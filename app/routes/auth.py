import os

from fastapi import APIRouter, Depends, HTTPException, Request, Response
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse

from ..auth import hash_password, verify_password, sign_session_token, verify_session_token, get_current_user
from ..crypto import make_fernet
from ..store import user_count, create_user, get_user
from ..models import SetupRequest, LoginRequest, LoginResponse

router = APIRouter()
fernet = make_fernet(os.environ["SECRET_KEY"])


def _cookie_secure() -> bool:
    val = os.environ.get("SECURE_COOKIE", "")
    if val:
        return val.lower() in ("true", "1", "yes")
    return os.environ.get("BASE_URL", "").startswith("https://")


@router.get("/auth/setup", response_class=HTMLResponse)
def setup_form():
    if user_count(fernet) > 0:
        return HTMLResponse("""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>Setup Already Done</title>
<style>
  *{box-sizing:border-box}
  body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;background:#f5f5f5;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0;padding:1rem}
  .card{background:white;padding:2rem;border-radius:12px;box-shadow:0 2px 8px rgba(0,0,0,0.1);text-align:center;max-width:400px;width:100%}
  .icon{font-size:2rem;margin-bottom:0.75rem}
  h1{color:#333;margin:0 0 0.5rem;font-size:1.25rem}
  p{color:#666;margin:0 0 1.25rem;font-size:0.9rem;line-height:1.5}
  a{color:#1976d2;text-decoration:none;font-weight:600}
  a:hover{text-decoration:underline}
</style>
</head>
<body><div class="card">
  <div class="icon">&#10003;</div>
  <h1>Setup Already Completed</h1>
  <p>An admin account has already been created. If you lost your credentials, use the CLI to create a new admin.</p>
  <p style="font-size:0.8rem;color:#999">CLI: <code style="font-size:0.75rem">python cli/manage.py user create email password --role admin</code></p>
  <p style="margin-top:1rem"><a href="/auth/login">Go to Login &rarr;</a></p>
</div></body>
</html>""")
    return HTMLResponse("""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Setup Admin</title>
<style>
  *{box-sizing:border-box}
  body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;background:#f5f5f5;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0;padding:1rem}
  .card{background:white;padding:1.5rem;border-radius:12px;box-shadow:0 2px 8px rgba(0,0,0,0.1);width:100%;max-width:400px}
  h1{margin:0 0 0.25rem;font-size:1.35rem;color:#333}
  p{margin:0 0 1.25rem;color:#666;font-size:0.9rem}
  label{display:block;margin-bottom:0.25rem;font-weight:600;color:#444;font-size:0.85rem}
  input{width:100%;padding:0.6rem;border:1px solid #ccc;border-radius:6px;font-size:1rem;margin-bottom:1rem;min-height:42px}
  input:focus{outline:none;border-color:#1976d2;box-shadow:0 0 0 2px rgba(25,118,210,0.2)}
  button{width:100%;padding:0.75rem;background:#1976d2;color:white;border:none;border-radius:6px;font-size:1rem;cursor:pointer;font-weight:600;min-height:44px;touch-action:manipulation}
  button:hover{background:#1565c0}
  .error{color:#d32f2f;font-size:0.85rem;margin-bottom:1rem;display:none;word-wrap:break-word}
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
      body: JSON.stringify({email: this.email.value.toLowerCase(), password: this.password.value})
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
def setup_submit(req: SetupRequest, response: Response):
    if user_count(fernet) > 0:
        raise HTTPException(400, "Admin already exists")
    password_hash = hash_password(req.password)
    user = create_user(fernet, req.email, password_hash, role="admin")
    token = sign_session_token(user.email, user.role)
    response.set_cookie(
        key="session",
        value=token,
        httponly=True,
        secure=_cookie_secure(),
        samesite="lax",
        max_age=86400,
    )
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
  body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;background:#f5f5f5;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0;padding:1rem}
  .card{background:white;padding:1.5rem;border-radius:12px;box-shadow:0 2px 8px rgba(0,0,0,0.1);width:100%;max-width:400px}
  h1{margin:0 0 1.25rem;font-size:1.35rem;color:#333}
  label{display:block;margin-bottom:0.25rem;font-weight:600;color:#444;font-size:0.85rem}
  input{width:100%;padding:0.6rem;border:1px solid #ccc;border-radius:6px;font-size:1rem;margin-bottom:1rem;min-height:42px}
  input:focus{outline:none;border-color:#1976d2;box-shadow:0 0 0 2px rgba(25,118,210,0.2)}
  button{width:100%;padding:0.75rem;background:#1976d2;color:white;border:none;border-radius:6px;font-size:1rem;cursor:pointer;font-weight:600;min-height:44px;touch-action:manipulation}
  button:hover{background:#1565c0}
  .error{color:#d32f2f;font-size:0.85rem;margin-bottom:1rem;display:none;word-wrap:break-word}
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
      body: JSON.stringify({email: this.email.value.toLowerCase(), password: this.password.value})
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
        secure=_cookie_secure(),
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
