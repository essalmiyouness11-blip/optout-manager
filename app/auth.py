import os
import secrets
from datetime import datetime, timedelta, timezone

import bcrypt
import jwt
from fastapi import HTTPException, Request
from fastapi import Depends

ALGORITHM = "HS256"
SESSION_EXPIRY_HOURS = 24


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def verify_password(password: str, password_hash: str) -> bool:
    return bcrypt.checkpw(password.encode(), password_hash.encode())


def generate_api_key() -> str:
    return secrets.token_hex(24)


def _session_secret() -> str:
    return os.environ["SECRET_KEY"]


def sign_session_token(email: str, role: str) -> str:
    payload = {
        "sub": email,
        "role": role,
        "iat": int(datetime.now(timezone.utc).timestamp()),
        "exp": int((datetime.now(timezone.utc) + timedelta(hours=SESSION_EXPIRY_HOURS)).timestamp()),
    }
    return jwt.encode(payload, _session_secret(), algorithm=ALGORITHM)


def verify_session_token(token: str) -> dict | None:
    try:
        return jwt.decode(token, _session_secret(), algorithms=[ALGORITHM])
    except jwt.PyJWTError:
        return None


def get_current_user(request: Request) -> dict:
    token = request.cookies.get("session")
    if not token:
        auth = request.headers.get("Authorization", "")
        if auth.startswith("Bearer "):
            token = auth[7:]
    if not token:
        raise HTTPException(401, "Not authenticated")
    payload = verify_session_token(token)
    if not payload:
        raise HTTPException(401, "Invalid or expired session")
    return payload


def require_admin(payload: dict = Depends(get_current_user)):
    if payload.get("role") != "admin":
        raise HTTPException(403, "Admin access required")
    return payload
