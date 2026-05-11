import json
import os
import threading
from datetime import datetime, timezone

from cryptography.fernet import Fernet

from .models import SuppressionStore, SuppressionEntry, UserEntry

_lock = threading.Lock()
_cache: SuppressionStore | None = None
_last_mtime: float = 0


def _store_path() -> str:
    return os.environ.get("SUPPRESSION_FILE", "data/suppressions.enc")


def _load(fernet: Fernet) -> SuppressionStore:
    global _cache, _last_mtime
    path = _store_path()
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)

    if not os.path.exists(path):
        _cache = SuppressionStore()
        return _cache

    mtime = os.path.getmtime(path)
    if _cache is not None and mtime <= _last_mtime:
        return _cache

    with open(path, "rb") as f:
        encrypted = f.read()
    decrypted = fernet.decrypt(encrypted).decode()
    data = json.loads(decrypted)
    _cache = SuppressionStore.model_validate(data)
    _last_mtime = mtime
    return _cache


def _save(fernet: Fernet, store: SuppressionStore) -> None:
    global _last_mtime
    path = _store_path()
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)

    raw = store.model_dump_json(by_alias=True)
    encrypted = fernet.encrypt(raw.encode())

    with open(path, "wb") as f:
        f.write(encrypted)
    _last_mtime = os.path.getmtime(path)


# ── Suppression functions ──

def _ensure_entry(store: SuppressionStore, h: str) -> SuppressionEntry:
    if h not in store.suppressions:
        store.suppressions[h] = SuppressionEntry()
    return store.suppressions[h]


def record_unsubscribe(
    fernet: Fernet,
    email_hash: str,
    level: str,
    target: str,
    target_name: str | None = None,
) -> dict:
    with _lock:
        store = _load(fernet)
        entry = _ensure_entry(store, email_hash)
        now = int(datetime.now(timezone.utc).timestamp())

        if level == "global":
            entry.global_ = True
            entry.networks.clear()
            entry.offers.clear()
        elif level == "network":
            entry.networks[target] = now
        elif level == "offer":
            entry.offers[target] = now

        hist_entry = {"level": level, "target": target, "at": now}
        if target_name:
            hist_entry["name"] = target_name
        entry.history.append(hist_entry)

        _save(fernet, store)
        return {"status": "ok", "level": level, "target": target}


def check_suppression(
    fernet: Fernet,
    email_hash: str,
    network: str | None = None,
    offer: str | None = None,
) -> bool:
    with _lock:
        store = _load(fernet)
        entry = store.suppressions.get(email_hash)
        if entry is None:
            return True
        if entry.global_:
            return False
        if network and network in entry.networks:
            return False
        if offer and offer in entry.offers:
            return False
        return True


def get_status(fernet: Fernet, email_hash: str) -> dict:
    with _lock:
        store = _load(fernet)
        entry = store.suppressions.get(email_hash)

    if entry is None:
        return {
            "email_hash": email_hash,
            "suppressed": False,
            "global_suppressed": False,
            "network_suppressions": [],
            "offer_suppressions": [],
        }
    return {
        "email_hash": email_hash,
        "suppressed": entry.global_ or bool(entry.networks) or bool(entry.offers),
        "global_suppressed": entry.global_,
        "network_suppressions": list(entry.networks.keys()),
        "offer_suppressions": list(entry.offers.keys()),
    }


def export_suppressions(fernet: Fernet) -> dict:
    with _lock:
        store = _load(fernet)
        return store.model_dump(by_alias=True)


def import_suppressions(fernet: Fernet, data: dict) -> int:
    with _lock:
        store = SuppressionStore.model_validate(data)
        _save(fernet, store)
        return len(store.suppressions)


# ── User functions ──

def _ensure_users(store: SuppressionStore):
    if store.users is None:
        store.users = {}


def user_count(fernet: Fernet) -> int:
    with _lock:
        store = _load(fernet)
        return len(store.users or {})


def create_user(fernet: Fernet, email: str, password_hash: str, role: str = "user") -> UserEntry:
    with _lock:
        store = _load(fernet)
        if email in (store.users or {}):
            raise ValueError("User already exists")
        from .auth import generate_api_key
        now = int(datetime.now(timezone.utc).timestamp())
        user = UserEntry(
            email=email,
            password_hash=password_hash,
            role=role,
            api_key=generate_api_key(),
            created_at=now,
        )
        store.users[email] = user
        _save(fernet, store)
        return user


def get_user(fernet: Fernet, email: str) -> UserEntry | None:
    with _lock:
        store = _load(fernet)
        return (store.users or {}).get(email)


def list_users(fernet: Fernet) -> list[UserEntry]:
    with _lock:
        store = _load(fernet)
        return list((store.users or {}).values())


def delete_user(fernet: Fernet, email: str) -> bool:
    with _lock:
        store = _load(fernet)
        if email not in (store.users or {}):
            return False
        del store.users[email]
        _save(fernet, store)
        return True


def update_user_api_key(fernet: Fernet, email: str) -> str:
    with _lock:
        store = _load(fernet)
        user = (store.users or {}).get(email)
        if not user:
            raise ValueError("User not found")
        from .auth import generate_api_key
        user.api_key = generate_api_key()
        _save(fernet, store)
        return user.api_key
