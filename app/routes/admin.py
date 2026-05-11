import os

from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse

from ..crypto import make_fernet, sign_unsubscribe_token, hash_email
from ..store import export_suppressions, import_suppressions, list_users, create_user, delete_user, update_user_api_key
from ..auth import hash_password, get_current_user, require_admin
from ..models import GenerateLinkRequest, GenerateLinkResponse, CreateUserRequest, UserResponse

router = APIRouter()
BASE_URL = os.environ.get("BASE_URL", "http://localhost:8000")

fernet = make_fernet(os.environ["SECRET_KEY"])


def _admin_or_api(request: Request, payload: dict = Depends(get_current_user)):
    return payload


@router.get("/admin", response_class=RedirectResponse)
def admin_root():
    return RedirectResponse(url="/admin/generate")


@router.get("/admin/generate", response_class=HTMLResponse)
def generate_form(payload: dict = Depends(get_current_user)):
    return HTMLResponse(f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Generate Unsubscribe Link</title>
<style>
  *{{box-sizing:border-box}}
  body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;background:#f5f5f5;margin:0;padding:0}}
  .nav{{background:#1a1a2e;color:white;padding:0.75rem 2rem;display:flex;justify-content:space-between;align-items:center}}
  .nav a{{color:#ccc;text-decoration:none;margin-left:1.5rem;font-size:0.875rem}}
  .nav a:hover{{color:white}}
  .nav .user{{font-size:0.8rem;color:#999}}
  .container{{max-width:600px;margin:2rem auto;padding:0 1rem}}
  .card{{background:white;padding:2rem;border-radius:12px;box-shadow:0 2px 8px rgba(0,0,0,0.1)}}
  h1{{margin:0 0 1.5rem;font-size:1.5rem;color:#333}}
  label{{display:block;margin-bottom:0.25rem;font-weight:600;color:#444;font-size:0.875rem}}
  input,select{{width:100%;padding:0.5rem;border:1px solid #ccc;border-radius:6px;font-size:1rem;margin-bottom:1rem}}
  input:focus,select:focus{{outline:none;border-color:#1976d2;box-shadow:0 0 0 2px rgba(25,118,210,0.2)}}
  button{{width:100%;padding:0.75rem;background:#1976d2;color:white;border:none;border-radius:6px;font-size:1rem;cursor:pointer;font-weight:600}}
  button:hover{{background:#1565c0}}
  .hidden{{display:none}}
  #result{{margin-top:1rem;padding:1rem;background:#e8f5e9;border-radius:6px;word-break:break-all;display:none}}
  #result a{{color:#1976d2}}
  .copy-btn{{margin-top:0.5rem;padding:0.4rem 0.75rem;background:#43a047;color:white;border:none;border-radius:4px;cursor:pointer;font-size:0.8rem}}
  .copy-btn:hover{{background:#388e3c}}
</style>
</head>
<body>
<div class="nav">
  <strong>Suppression Manager</strong>
  <div>
    <a href="/admin/generate">Generate</a>
    <a href="/admin/users">Users</a>
    <span class="user">{payload['sub']} ({payload['role']})</span>
    <a href="/auth/logout" onclick="fetch('/auth/logout',{{method:'POST'}}).then(()=>location.href='/auth/login');return false">Logout</a>
  </div>
</div>
<div class="container">
<div class="card">
  <h1>Generate Unsubscribe Link</h1>
  <form id="form">
    <label for="email">Email</label>
    <input type="email" id="email" name="email" required placeholder="user@example.com">
    <label for="level">Level</label>
    <select id="level" name="level">
      <option value="global">Global (all communications)</option>
      <option value="network">Network</option>
      <option value="offer">Offer</option>
    </select>
    <div id="network-field" class="hidden">
      <label for="network_id">Network ID</label>
      <input type="text" id="network_id" name="network_id" placeholder="e.g. net_42">
    </div>
    <div id="offer-field" class="hidden">
      <label for="offer_id">Offer ID</label>
      <input type="text" id="offer_id" name="offer_id" placeholder="e.g. off_789">
    </div>
    <button type="submit">Generate Link</button>
  </form>
  <div id="result">
    <strong>Unsubscribe URL:</strong><br>
    <a id="result-url" href="#" target="_blank"></a><br><br>
    <strong>Token:</strong><br>
    <code id="result-token" style="font-size:0.8rem;word-break:break-all;"></code><br><br>
    <button class="copy-btn" onclick="navigator.clipboard.writeText(document.getElementById('result-url').href).then(()=>alert('Copied!'))">Copy URL</button>
  </div>
</div>
</div>
<script>
  document.getElementById('level').addEventListener('change',function(){{
    document.getElementById('network-field').classList.toggle('hidden',this.value!=='network');
    document.getElementById('offer-field').classList.toggle('hidden',this.value!=='offer');
  }});
  document.getElementById('form').addEventListener('submit',async function(e){{
    e.preventDefault();
    const body={{email:this.email.value,level:this.level.value,network_id:document.getElementById('network_id').value||null,offer_id:document.getElementById('offer_id').value||null}};
    const res=await fetch('/admin/generate',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify(body)}});
    if(!res.ok){{const d=await res.json();alert('Error: '+(d.detail||'Unknown'));return;}}
    const data=await res.json();
    document.getElementById('result-url').href=data.unsubscribe_url;
    document.getElementById('result-url').textContent=data.unsubscribe_url;
    document.getElementById('result-token').textContent=data.token;
    document.getElementById('result').style.display='block';
  }});
</script>
</body>
</html>""")


@router.post("/admin/generate", response_model=GenerateLinkResponse)
def generate_link(req: GenerateLinkRequest, _=Depends(get_current_user)):
    secret = os.environ["SECRET_KEY"]
    h = hash_email(req.email)
    if req.level == "global":
        target = "*"
    elif req.level == "network":
        if not req.network_id:
            raise HTTPException(400, "network_id required")
        target = req.network_id
    elif req.level == "offer":
        if not req.offer_id:
            raise HTTPException(400, "offer_id required")
        target = req.offer_id
    else:
        raise HTTPException(400, "Invalid level")
    token = sign_unsubscribe_token(secret, h, req.level, target)
    url = f"{BASE_URL}/u?t={token}"
    return GenerateLinkResponse(unsubscribe_url=url, token=token)


@router.get("/admin/users", response_class=HTMLResponse)
def users_page(payload: dict = Depends(require_admin)):
    users = list_users(fernet)
    rows = "".join(
        f"<tr><td>{u.email}</td><td>{u.role}</td><td><code style='font-size:0.75rem'>{u.api_key[:16]}...</code></td>"
        f"<td>{u.created_at}</td>"
        f"<td><button class='del' data-email='{u.email}'>Delete</button></td></tr>"
        for u in users
    )
    return HTMLResponse(f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Manage Users</title>
<style>
  *{{box-sizing:border-box}}
  body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;background:#f5f5f5;margin:0;padding:0}}
  .nav{{background:#1a1a2e;color:white;padding:0.75rem 2rem;display:flex;justify-content:space-between;align-items:center}}
  .nav a{{color:#ccc;text-decoration:none;margin-left:1.5rem;font-size:0.875rem}}
  .nav a:hover{{color:white}}
  .container{{max-width:800px;margin:2rem auto;padding:0 1rem}}
  .card{{background:white;padding:2rem;border-radius:12px;box-shadow:0 2px 8px rgba(0,0,0,0.1);margin-bottom:1rem}}
  h1{{margin:0 0 1.5rem;font-size:1.5rem;color:#333}}
  table{{width:100%;border-collapse:collapse}}
  th,td{{text-align:left;padding:0.5rem;border-bottom:1px solid #eee;font-size:0.875rem}}
  th{{font-weight:600;color:#444}}
  input{{padding:0.5rem;border:1px solid #ccc;border-radius:6px;font-size:0.875rem;margin-right:0.5rem}}
  select{{padding:0.5rem;border:1px solid #ccc;border-radius:6px;font-size:0.875rem;margin-right:0.5rem}}
  .btn{{padding:0.5rem 1rem;background:#1976d2;color:white;border:none;border-radius:6px;cursor:pointer;font-size:0.875rem}}
  .btn:hover{{background:#1565c0}}
  .del{{padding:0.5rem 1rem;background:#d32f2f;color:white;border:none;border-radius:6px;cursor:pointer;font-size:0.875rem}}
  .del:hover{{background:#b71c1c}}
  #msg{{margin-top:1rem;padding:0.75rem;border-radius:6px;display:none}}
  .success{{background:#e8f5e9;color:#2e7d32}}
  .error{{background:#ffebee;color:#d32f2f}}
</style>
</head>
<body>
<div class="nav">
  <strong>Suppression Manager</strong>
  <div>
    <a href="/admin/generate">Generate</a>
    <a href="/admin/users">Users</a>
    <a href="/auth/logout" onclick="fetch('/auth/logout',{{method:'POST'}}).then(()=>location.href='/auth/login');return false">Logout</a>
  </div>
</div>
<div class="container">
<div class="card">
  <h1>Users</h1>
  <table>
    <thead><tr><th>Email</th><th>Role</th><th>API Key</th><th>Created</th><th></th></tr></thead>
    <tbody>{rows}</tbody>
  </table>
</div>
<div class="card">
  <h2>Add User</h2>
  <input type="email" id="new-email" placeholder="Email">
  <input type="password" id="new-pw" placeholder="Password (min 8 chars)">
  <select id="new-role">
    <option value="user">User</option>
    <option value="admin">Admin</option>
  </select>
  <button class="btn" onclick="addUser()">Add</button>
  <div id="msg"></div>
</div>
</div>
<script>
  function msg(text,type){{const el=document.getElementById('msg');el.textContent=text;el.className=type;el.style.display='block';setTimeout(()=>el.style.display='none',3000)}}
  async function addUser(){{
    const email=document.getElementById('new-email').value;
    const pw=document.getElementById('new-pw').value;
    const role=document.getElementById('new-role').value;
    if(!email||!pw)return;
    const res=await fetch('/admin/users',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{email,password:pw,role}})}});
    if(!res.ok){{const d=await res.json();msg(d.detail||'Error','error');return;}}
    msg('User created','success');location.reload();
  }}
  document.querySelectorAll('.del').forEach(b=>b.addEventListener('click',async function(){{
    if(!confirm('Delete '+this.dataset.email+'?'))return;
    const res=await fetch('/admin/users/'+encodeURIComponent(this.dataset.email),{{method:'DELETE'}});
    if(!res.ok){{const d=await res.json();msg(d.detail||'Error','error');return;}}
    msg('User deleted','success');location.reload();
  }}));
</script>
</body>
</html>""")


@router.post("/admin/users")
def create_user_endpoint(req: CreateUserRequest, _=Depends(require_admin)):
    pw_hash = hash_password(req.password)
    user = create_user(fernet, req.email, pw_hash, req.role)
    return UserResponse(email=user.email, role=user.role, api_key=user.api_key, created_at=user.created_at)


@router.delete("/admin/users/{email}")
def delete_user_endpoint(email: str, _=Depends(require_admin)):
    if not delete_user(fernet, email):
        raise HTTPException(404, "User not found")
    return {"status": "deleted"}


@router.get("/admin/export")
def admin_export(_=Depends(require_admin)):
    return JSONResponse(content=export_suppressions(fernet))


@router.post("/admin/import")
def admin_import(data: dict, _=Depends(require_admin)):
    count = import_suppressions(fernet, data)
    return {"imported": count}
