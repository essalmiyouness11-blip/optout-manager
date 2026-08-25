import os

from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import HTMLResponse, RedirectResponse

from ..crypto import verify_unsubscribe_token, make_fernet, hash_email
from ..store import record_unsubscribe, check_suppression, get_network, get_offer
from ..models import CheckRequest, CheckResponse, UnsubscribeFormRequest
from ..templates import random_email_form, random_success

router = APIRouter()


def _get_fernet():
    return make_fernet(os.environ["SECRET_KEY"])


def _lookup_target_name(fernet, level: str, target: str) -> str | None:
    if level == "network":
        net = get_network(fernet, target)
        return net.name if net else None
    elif level == "offer":
        off = get_offer(fernet, target)
        return off.name if off else None
    return None


@router.get("/u/success", response_class=HTMLResponse)
def unsubscribe_success():
    return HTMLResponse(random_success())


@router.get("/u", response_class=HTMLResponse)
def unsubscribe_get(token: str = Query(..., alias="t"), email: str = Query(None, alias="e")):
    secret = os.environ["SECRET_KEY"]
    payload = verify_unsubscribe_token(secret, token)
    if payload is None:
        return HTMLResponse("<h1>Invalid or expired link</h1>", status_code=400)

    level = payload.get("l")
    target = payload.get("t")
    if not level or not target:
        return HTMLResponse("<h1>Invalid or expired link</h1>", status_code=400)

    # Token has email hash → auto-unsubscribe (no email stored)
    if payload.get("h"):
        fernet = _get_fernet()
        record_unsubscribe(fernet, payload["h"], level, target)
        return RedirectResponse(url="/u/success", status_code=302)

    # Email provided in query → auto-unsubscribe
    if email:
        fernet = _get_fernet()
        h = hash_email(email)
        target_name = _lookup_target_name(fernet, level, target)
        record_unsubscribe(fernet, h, level, target, target_name=target_name, email=email)
        return RedirectResponse(url="/u/success", status_code=302)

    # Show random themed form
    return HTMLResponse(random_email_form(token))


@router.post("/u")
def unsubscribe_submit(req: UnsubscribeFormRequest):
    secret = os.environ["SECRET_KEY"]
    payload = verify_unsubscribe_token(secret, req.token)
    if payload is None:
        raise HTTPException(400, "Invalid or expired token")

    level = payload.get("l")
    target = payload.get("t")
    if not level or not target:
        raise HTTPException(400, "Invalid or expired token")

    fernet = _get_fernet()
    h = hash_email(req.email)
    target_name = _lookup_target_name(fernet, level, target)
    record_unsubscribe(fernet, h, level, target, target_name=target_name, email=req.email)

    return {"status": "ok", "message": "Unsubscribed"}


@router.post("/check", response_model=CheckResponse)
def check(req: CheckRequest):
    fernet = _get_fernet()
    allowed = check_suppression(fernet, req.h, req.network, req.offer)
    return CheckResponse(allowed=allowed)
