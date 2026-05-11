import os

from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import HTMLResponse

from ..crypto import verify_unsubscribe_token, make_fernet, hash_email
from ..store import record_unsubscribe, check_suppression
from ..models import CheckRequest, CheckResponse, UnsubscribeFormRequest

router = APIRouter()


def _get_fernet():
    return make_fernet(os.environ["SECRET_KEY"])


def _unsub_page(message: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Unsubscribed</title>
<style>
  body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0;background:#f5f5f5}}
  .card{{background:white;padding:2rem;border-radius:12px;box-shadow:0 2px 4px rgba(0,0,0,0.1);text-align:center;max-width:400px}}
  h1{{color:#2e7d32;margin:0 0 0.5rem}}
  p{{color:#555;line-height:1.5;margin:0.5rem 0}}
</style>
</head>
<body>
<div class="card">
  <h1>Unsubscribed</h1>
  <p>{message}</p>
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
  body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0;background:#f5f5f5}}
  .card{{background:white;padding:2rem;border-radius:12px;box-shadow:0 2px 4px rgba(0,0,0,0.1);text-align:center;max-width:380px}}
  h1{{color:#333;margin:0 0 0.25rem;font-size:1.3rem}}
  p{{color:#666;margin:0.5rem 0 1.25rem;font-size:0.9rem}}
  input{{width:100%;padding:0.6rem;border:1px solid #ccc;border-radius:6px;font-size:1rem;margin-bottom:0.75rem}}
  input:focus{{outline:none;border-color:#1976d2;box-shadow:0 0 0 2px rgba(25,118,210,0.2)}}
  button{{width:100%;padding:0.7rem;background:#d32f2f;color:white;border:none;border-radius:6px;font-size:1rem;cursor:pointer;font-weight:600}}
  button:hover{{background:#b71c1c}}
  .error{{color:#d32f2f;font-size:0.85rem;margin-bottom:0.5rem;display:none}}
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
    const res = await fetch('/u', {{
      method: 'POST',
      headers: {{'Content-Type': 'application/json'}},
      body: JSON.stringify({{token: '{token}', email: this.email.value}})
    }});
    if (res.ok) {{ location.reload(); return; }}
    const data = await res.json();
    document.getElementById('error').textContent = data.detail || 'Error';
    document.getElementById('error').style.display = 'block';
  }});
</script>
</body>
</html>"""


@router.get("/u", response_class=HTMLResponse)
def unsubscribe_get(token: str = Query(..., alias="t"), email: str = Query(None, alias="e")):
    secret = os.environ["SECRET_KEY"]
    payload = verify_unsubscribe_token(secret, token)
    if payload is None:
        return HTMLResponse("<h1>Invalid or expired link</h1>", status_code=400)

    level = payload["l"]
    target = payload["t"]

    # Token has email hash → auto-unsubscribe
    if payload.get("h"):
        fernet = _get_fernet()
        record_unsubscribe(fernet, payload["h"], level, target)
        return HTMLResponse(_unsub_page("You have been unsubscribed."))

    # Email provided in query → auto-unsubscribe
    if email:
        fernet = _get_fernet()
        h = hash_email(email)
        record_unsubscribe(fernet, h, level, target)
        return HTMLResponse(_unsub_page("You have been unsubscribed."))

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
    record_unsubscribe(fernet, h, payload["l"], payload["t"])

    return {"status": "ok", "message": "Unsubscribed"}


@router.post("/check", response_model=CheckResponse)
def check(req: CheckRequest):
    fernet = _get_fernet()
    allowed = check_suppression(fernet, req.h, req.network, req.offer)
    return CheckResponse(allowed=allowed)
