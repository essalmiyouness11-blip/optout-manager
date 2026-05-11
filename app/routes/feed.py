import os

from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import JSONResponse

from ..crypto import make_fernet
from ..store import get_unsubscribers_for_target, get_feed_token, get_offer_csv_data

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


@router.get("/feed/unsubscribers/{target}/csv")
def feed_unsubscribers_csv(
    target: str,
    token: str = Query(...),
    level: str = Query("offer"),
    format: str = Query("plain"),
    since: int = Query(0),
):
    if level not in ("network", "offer"):
        raise HTTPException(400, "Level must be 'network' or 'offer'")

    expected = get_feed_token(fernet, level, target)
    if not expected or token != expected:
        raise HTTPException(403, "Invalid feed token")

    if level == "offer":
        csv = get_offer_csv_data(fernet, target, format, since)
    else:
        results = get_unsubscribers_for_target(fernet, level, target, since)
        if format == "md5":
            lines = ["md5_email,timestamp"]
            for r in results:
                md5 = r.get("md5") or ""
                lines.append(f'{md5},{r["timestamp"]}')
        else:
            lines = ["email,md5,sha256,timestamp"]
            for r in results:
                lines.append(f'{r.get("email","")},{r.get("md5","")},{r["email_hash"]},{r["timestamp"]}')
        csv = "\n".join(lines) + "\n"

    from fastapi.responses import Response
    suffix = "md5" if format == "md5" else "full"
    return Response(
        content=csv,
        media_type="text/csv",
        headers={"Content-Disposition": f"attachment; filename={level}_{target}_unsubscribers_{suffix}.csv"},
    )
