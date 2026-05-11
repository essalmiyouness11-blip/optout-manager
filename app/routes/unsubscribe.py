import os

from fastapi import APIRouter, Query
from fastapi.responses import HTMLResponse

from ..crypto import verify_unsubscribe_token, make_fernet
from ..store import record_unsubscribe, check_suppression
from ..models import CheckRequest, CheckResponse

router = APIRouter()


def _get_fernet():
    return make_fernet(os.environ["SECRET_KEY"])


@router.get("/u", response_class=HTMLResponse)
def unsubscribe_via_link(token: str = Query(..., alias="t")):
    secret = os.environ["SECRET_KEY"]
    payload = verify_unsubscribe_token(secret, token)
    if payload is None:
        return HTMLResponse("<h1>Invalid or expired link</h1>", status_code=400)

    fernet = _get_fernet()
    result = record_unsubscribe(fernet, payload["h"], payload["l"], payload["t"])

    level_labels = {"global": "all emails", "network": f"network {payload['t']}", "offer": f"offer {payload['t']}"}
    label = level_labels.get(payload["l"], payload["t"])

    html = f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Unsubscribed</title>
<style>
  body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; background: #f5f5f5; }}
  .card {{ background: white; padding: 2rem; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); text-align: center; max-width: 400px; }}
  h1 {{ color: #2e7d32; margin: 0 0 0.5rem; }}
  p {{ color: #555; line-height: 1.5; }}
</style>
</head>
<body>
<div class="card">
  <h1>Unsubscribed</h1>
  <p>You have been unsubscribed from <strong>{label}</strong>.</p>
</div>
</body>
</html>"""
    return HTMLResponse(html)


@router.post("/check", response_model=CheckResponse)
def check(req: CheckRequest):
    fernet = _get_fernet()
    allowed = check_suppression(fernet, req.h, req.network, req.offer)
    return CheckResponse(allowed=allowed)
