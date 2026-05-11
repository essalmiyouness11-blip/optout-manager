import hashlib
import os
from datetime import datetime, timezone

import jwt
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64

ALGORITHM = "HS256"
JWT_EXPIRATION_DAYS = 365 * 5


def _derive_fernet_key(master_secret: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=600_000,
    )
    return base64.urlsafe_b64encode(kdf.derive(master_secret.encode()))


def make_fernet(master_secret: str) -> Fernet:
    salt = b"suppression-manager-v1-fixed-salt"
    key = _derive_fernet_key(master_secret, salt)
    return Fernet(key)


def hash_email(email: str) -> str:
    return hashlib.sha256(email.strip().lower().encode()).hexdigest()


def md5_email(email: str) -> str:
    return hashlib.md5(email.strip().lower().encode()).hexdigest()


def sign_unsubscribe_token(
    secret: str,
    level: str,
    target: str,
    target_name: str | None = None,
    email_hash: str | None = None,
) -> str:
    payload = {
        "l": level,
        "t": target,
        "j": os.urandom(8).hex(),
        "i": int(datetime.now(timezone.utc).timestamp()),
    }
    if email_hash:
        payload["h"] = email_hash
    if target_name:
        payload["n"] = target_name
    return jwt.encode(payload, secret, algorithm=ALGORITHM)


def verify_unsubscribe_token(secret: str, token: str) -> dict | None:
    try:
        return jwt.decode(token, secret, algorithms=[ALGORITHM])
    except jwt.PyJWTError:
        return None
