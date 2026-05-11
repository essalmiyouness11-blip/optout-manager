import os

from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import HTMLResponse, RedirectResponse

from ..crypto import verify_unsubscribe_token, make_fernet, hash_email
from ..store import record_unsubscribe, check_suppression
from ..models import CheckRequest, CheckResponse, UnsubscribeFormRequest

router = APIRouter()


def _get_fernet():
    return make_fernet(os.environ["SECRET_KEY"])


_SUCCESS_HTML = """<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unsubscribed</title>
<style>
  *{box-sizing:border-box}
  body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0;background:#f5f5f5;padding:1rem}
  .card{background:white;padding:2.5rem 2rem;border-radius:16px;box-shadow:0 4px 24px rgba(0,0,0,0.08);text-align:center;max-width:420px;width:100%;animation:fadeIn .4s ease}
  @keyframes fadeIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:translateY(0)}}
  .icon{width:56px;height:56px;border-radius:50%;background:#e8f5e9;display:flex;align-items:center;justify-content:center;margin:0 auto 1.25rem}
  .icon svg{width:28px;height:28px}
  h1{color:#1b1b1b;margin:0 0 0.5rem;font-size:1.35rem;font-weight:700}
  p{color:#5f6368;line-height:1.6;margin:0 0 0.25rem;font-size:0.95rem}
  .muted{color:#9aa0a6;font-size:0.8rem;margin-top:1.25rem}
</style>
</head>
<body>
<div class="card">
  <div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="#2e7d32" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg></div>
  <h1>You're unsubscribed</h1>
  <p>You have been successfully removed from our mailing list.</p>
  <p class="muted">You can safely close this page.</p>
</div>
</body>
</html>"""


def _email_form(token: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Unsubscribe</title>
<style>
  *{{box-sizing:border-box}}
  body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0;background:#f5f5f5;padding:1rem}}
  .card{{background:white;padding:1.5rem;border-radius:12px;box-shadow:0 2px 4px rgba(0,0,0,0.1);text-align:center;max-width:380px;width:100%}}
  h1{{color:#333;margin:0 0 0.25rem;font-size:1.25rem}}
  p{{color:#666;margin:0.5rem 0 1.25rem;font-size:0.9rem}}
  input{{width:100%;padding:0.65rem;border:1px solid #ccc;border-radius:6px;font-size:1rem;margin-bottom:0.75rem;min-height:42px}}
  input:focus{{outline:none;border-color:#1976d2;box-shadow:0 0 0 2px rgba(25,118,210,0.2)}}
  button{{width:100%;padding:0.7rem;background:#d32f2f;color:white;border:none;border-radius:6px;font-size:1rem;cursor:pointer;font-weight:600;min-height:44px;touch-action:manipulation}}
  button:hover{{background:#b71c1c}}
  .error{{color:#d32f2f;font-size:0.85rem;margin-bottom:0.5rem;display:none;word-wrap:break-word}}
</style>
</head>
<body>
<div class="card">
  <h1>Unsubscribe</h1>
  <p>Enter your email address to unsubscribe.</p>
  <div class="error" id="error"></div>
  <form id="form">
    <input type="email" id="email" name="email" required placeholder="your@email.com">
    <button type="submit">Unsubscribe</button>
  </form>
</div>
<script>
  document.getElementById('form').addEventListener('submit', async function(e) {{
    e.preventDefault();
    const btn = this.querySelector('button');
    btn.disabled = true; btn.textContent = 'Processing...';
    try {{
      const res = await fetch('/u', {{
        method: 'POST',
        headers: {{'Content-Type': 'application/json'}},
        body: JSON.stringify({{token: '{token}', email: this.email.value.toLowerCase()}})
      }});
      if (res.ok) {{ window.location.href = '/u/success'; return; }}
      const data = await res.json();
      document.getElementById('error').textContent = data.detail || 'Error';
      document.getElementById('error').style.display = 'block';
    }} finally {{ btn.disabled = false; btn.textContent = 'Unsubscribe'; }}
  }});
</script>
</body>
</html>"""


@router.get("/u/success", response_class=HTMLResponse)
def unsubscribe_success():
    return HTMLResponse(_SUCCESS_HTML)


@router.get("/u", response_class=HTMLResponse)
def unsubscribe_get(token: str = Query(..., alias="t"), email: str = Query(None, alias="e")):
    secret = os.environ["SECRET_KEY"]
    payload = verify_unsubscribe_token(secret, token)
    if payload is None:
        return HTMLResponse("<h1>Invalid or expired link</h1>", status_code=400)

    level = payload["l"]
    target = payload["t"]

    # Token has email hash → auto-unsubscribe (no email stored)
    if payload.get("h"):
        fernet = _get_fernet()
        record_unsubscribe(fernet, payload["h"], level, target)
        return RedirectResponse(url="/u/success", status_code=302)

    # Email provided in query → auto-unsubscribe
    if email:
        fernet = _get_fernet()
        h = hash_email(email)
        record_unsubscribe(fernet, h, level, target, email=email)
        return RedirectResponse(url="/u/success", status_code=302)

    # Show clean form (no offer/network info)
    return HTMLResponse(_email_form(token))


@router.post("/u")
def unsubscribe_submit(req: UnsubscribeFormRequest):
    secret = os.environ["SECRET_KEY"]
    payload = verify_unsubscribe_token(secret, req.token)
    if payload is None:
        raise HTTPException(400, "Invalid or expired token")

    fernet = _get_fernet()
    h = hash_email(req.email)
    record_unsubscribe(fernet, h, payload["l"], payload["t"], email=req.email)

    return {"status": "ok", "message": "Unsubscribed"}


@router.post("/check", response_model=CheckResponse)
def check(req: CheckRequest):
    fernet = _get_fernet()
    allowed = check_suppression(fernet, req.h, req.network, req.offer)
    return CheckResponse(allowed=allowed)
