import os

from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import JSONResponse

from ..crypto import make_fernet
from ..store import get_unsubscribers_for_target, get_feed_token

router = APIRouter()
fernet = make_fernet(os.environ["SECRET_KEY"])


@router.get("/feed/unsubscribers/{target}")
def feed_unsubscribers(
    target: str,
    token: str = Query(...),
    level: str = Query("offer"),
    since: int = Query(0),
):
    if level not in ("network", "offer"):
        raise HTTPException(400, "Level must be 'network' or 'offer'")

    expected = get_feed_token(fernet, level, target)
    if not expected or token != expected:
        raise HTTPException(403, "Invalid feed token")

    results = get_unsubscribers_for_target(fernet, level, target, since)

    return {
        "target": target,
        "level": level,
        "generated_at": int(__import__("time").time()),
        "count": len(results),
        "unsubscribers": results,
    }
