import os

from fastapi import APIRouter, Depends, HTTPException, Request, Response
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse

from ..auth import hash_password, verify_password, sign_session_token, verify_session_token, get_current_user
from ..crypto import make_fernet
from ..store import user_count, create_user, get_user
from ..models import SetupRequest, LoginRequest, LoginResponse

router = APIRouter()
fernet = make_fernet(os.environ["SECRET_KEY"])


@router.get("/auth/setup", response_class=HTMLResponse)
def setup_form():
    if user_count(fernet) > 0:
        return RedirectResponse(url="/auth/login")
    return HTMLResponse("""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Setup Admin</title>
<style>
  *{box-sizing:border-box}
  body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;background:#f5f5f5;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
  .card{background:white;padding:2rem;border-radius:12px;box-shadow:0 2px 8px rgba(0,0,0,0.1);width:100%;max-width:400px}
  h1{margin:0 0 0.25rem;font-size:1.5rem;color:#333}
  p{margin:0 0 1.5rem;color:#666}
  label{display:block;margin-bottom:0.25rem;font-weight:600;color:#444;font-size:0.875rem}
  input{width:100%;padding:0.5rem;border:1px solid #ccc;border-radius:6px;font-size:1rem;margin-bottom:1rem}
  input:focus{outline:none;border-color:#1976d2;box-shadow:0 0 0 2px rgba(25,118,210,0.2)}
  button{width:100%;padding:0.75rem;background:#1976d2;color:white;border:none;border-radius:6px;font-size:1rem;cursor:pointer;font-weight:600}
  button:hover{background:#1565c0}
  .error{color:#d32f2f;font-size:0.875rem;margin-bottom:1rem;display:none}
</style>
</head>
<body>
<div class="card">
  <h1>Setup Admin Account</h1>
  <p>Create the first administrator account</p>
  <div class="error" id="error"></div>
  <form id="form">
    <label for="email">Email</label>
    <input type="email" id="email" name="email" required>
    <label for="password">Password (min 8 chars)</label>
    <input type="password" id="password" name="password" required minlength="8">
    <button type="submit">Create Admin</button>
  </form>
</div>
<script>
  document.getElementById('form').addEventListener('submit', async function(e) {
    e.preventDefault();
    const res = await fetch('/auth/setup', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({email: this.email.value, password: this.password.value})
    });
    if (res.ok) { window.location.href = '/admin'; return; }
    const data = await res.json();
    document.getElementById('error').textContent = data.detail || 'Error';
    document.getElementById('error').style.display = 'block';
  });
</script>
</body>
</html>""")


@router.post("/auth/setup")
def setup_submit(req: SetupRequest):
    if user_count(fernet) > 0:
        raise HTTPException(400, "Admin already exists")
    password_hash = hash_password(req.password)
    user = create_user(fernet, req.email, password_hash, role="admin")
    token = sign_session_token(user.email, user.role)
    return LoginResponse(token=token, email=user.email, role=user.role)


@router.get("/auth/login", response_class=HTMLResponse)
def login_form():
    return HTMLResponse("""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Login</title>
<style>
  *{box-sizing:border-box}
  body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;background:#f5f5f5;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
  .card{background:white;padding:2rem;border-radius:12px;box-shadow:0 2px 8px rgba(0,0,0,0.1);width:100%;max-width:400px}
  h1{margin:0 0 1.5rem;font-size:1.5rem;color:#333}
  label{display:block;margin-bottom:0.25rem;font-weight:600;color:#444;font-size:0.875rem}
  input{width:100%;padding:0.5rem;border:1px solid #ccc;border-radius:6px;font-size:1rem;margin-bottom:1rem}
  input:focus{outline:none;border-color:#1976d2;box-shadow:0 0 0 2px rgba(25,118,210,0.2)}
  button{width:100%;padding:0.75rem;background:#1976d2;color:white;border:none;border-radius:6px;font-size:1rem;cursor:pointer;font-weight:600}
  button:hover{background:#1565c0}
  .error{color:#d32f2f;font-size:0.875rem;margin-bottom:1rem;display:none}
</style>
</head>
<body>
<div class="card">
  <h1>Login</h1>
  <div class="error" id="error"></div>
  <form id="form">
    <label for="email">Email</label>
    <input type="email" id="email" name="email" required>
    <label for="password">Password</label>
    <input type="password" id="password" name="password" required>
    <button type="submit">Sign In</button>
  </form>
</div>
<script>
  document.getElementById('form').addEventListener('submit', async function(e) {
    e.preventDefault();
    const res = await fetch('/auth/login', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({email: this.email.value, password: this.password.value})
    });
    if (res.ok) { window.location.href = '/admin'; return; }
    const data = await res.json();
    document.getElementById('error').textContent = data.detail || 'Invalid credentials';
    document.getElementById('error').style.display = 'block';
  });
</script>
</body>
</html>""")


@router.post("/auth/login")
def login_submit(req: LoginRequest, response: Response):
    user = get_user(fernet, req.email)
    if not user or not verify_password(req.password, user.password_hash):
        raise HTTPException(401, "Invalid email or password")
    token = sign_session_token(user.email, user.role)
    response.set_cookie(
        key="session",
        value=token,
        httponly=True,
        secure=False,
        samesite="lax",
        max_age=86400,
    )
    return LoginResponse(token=token, email=user.email, role=user.role)


@router.post("/auth/logout")
def logout(response: Response):
    response.delete_cookie("session")
    return {"status": "ok"}


@router.get("/auth/me")
def me(payload: dict = Depends(get_current_user)):
    return {"email": payload["sub"], "role": payload["role"]}
