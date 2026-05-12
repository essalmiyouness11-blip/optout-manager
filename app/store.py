import json
import os
import threading
from datetime import datetime, timezone

from cryptography.fernet import Fernet

from .models import SuppressionStore, SuppressionEntry, UserEntry, AffiliateNetworkEntry, OfferEntry

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
    email: str | None = None,
) -> dict:
    with _lock:
        store = _load(fernet)
        entry = _ensure_entry(store, email_hash)
        now = int(datetime.now(timezone.utc).timestamp())

        md5_val = ""
        if email:
            email_lower = email.strip().lower()
            entry.email = email_lower
            from .crypto import md5_email
            md5_val = md5_email(email_lower)
            entry.md5 = md5_val

        if level == "global":
            entry.global_ = now
            entry.networks.clear()
            entry.offers.clear()
        elif level == "network":
            entry.networks[target] = now
        elif level == "offer":
            entry.offers[target] = now
            # also store email/MD5 in the offer's own list
            if email and target in (store.offers or {}):
                offer = store.offers[target]
                # avoid duplicates by sha256
                existing = {r.get("sha256", "") for r in offer.unsubscribers}
                if email_hash not in existing:
                    offer.unsubscribers.append({
                        "email": email_lower,
                        "md5": md5_val,
                        "sha256": email_hash,
                        "timestamp": now,
                    })

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
        "global_suppressed": bool(entry.global_),
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


# ── Affiliate Network CRUD ──

def create_network(fernet: Fernet, net_id: str, name: str) -> AffiliateNetworkEntry:
    with _lock:
        store = _load(fernet)
        if net_id in (store.networks or {}):
            raise ValueError("Network already exists")
        now = int(datetime.now(timezone.utc).timestamp())
        net = AffiliateNetworkEntry(id=net_id, name=name, created_at=now)
        store.networks[net_id] = net
        _save(fernet, store)
        return net


def get_network(fernet: Fernet, net_id: str) -> AffiliateNetworkEntry | None:
    with _lock:
        store = _load(fernet)
        return (store.networks or {}).get(net_id)


def list_networks(fernet: Fernet) -> list[AffiliateNetworkEntry]:
    with _lock:
        store = _load(fernet)
        return list((store.networks or {}).values())


def update_network(fernet: Fernet, net_id: str, name: str) -> AffiliateNetworkEntry | None:
    with _lock:
        store = _load(fernet)
        net = (store.networks or {}).get(net_id)
        if not net:
            return None
        net.name = name
        _save(fernet, store)
        return net


def delete_network(fernet: Fernet, net_id: str) -> bool:
    with _lock:
        store = _load(fernet)
        if net_id not in (store.networks or {}):
            return False
        del store.networks[net_id]
        # also remove all offers belonging to this network
        to_remove = [oid for oid, o in (store.offers or {}).items() if o.network_id == net_id]
        for oid in to_remove:
            del store.offers[oid]
        _save(fernet, store)
        return True


# ── Offer CRUD ──

def create_offer(fernet: Fernet, offer_id: str, name: str, network_id: str) -> OfferEntry:
    with _lock:
        store = _load(fernet)
        if offer_id in (store.offers or {}):
            raise ValueError("Offer already exists")
        if network_id not in (store.networks or {}):
            raise ValueError("Network not found")
        now = int(datetime.now(timezone.utc).timestamp())
        offer = OfferEntry(id=offer_id, name=name, network_id=network_id, created_at=now)
        store.offers[offer_id] = offer
        _save(fernet, store)
        return offer


def get_offer(fernet: Fernet, offer_id: str) -> OfferEntry | None:
    with _lock:
        store = _load(fernet)
        return (store.offers or {}).get(offer_id)


def list_offers(fernet: Fernet, network_id: str | None = None) -> list[OfferEntry]:
    with _lock:
        store = _load(fernet)
        all_offers = list((store.offers or {}).values())
    if network_id:
        return [o for o in all_offers if o.network_id == network_id]
    return all_offers


def update_offer(fernet: Fernet, offer_id: str, name: str) -> OfferEntry | None:
    with _lock:
        store = _load(fernet)
        offer = (store.offers or {}).get(offer_id)
        if not offer:
            return None
        offer.name = name
        _save(fernet, store)
        return offer


def delete_offer(fernet: Fernet, offer_id: str) -> bool:
    with _lock:
        store = _load(fernet)
        if offer_id not in (store.offers or {}):
            return False
        del store.offers[offer_id]
        _save(fernet, store)
        return True


# ── Dashboard ──

def get_dashboard(fernet: Fernet) -> dict:
    with _lock:
        store = _load(fernet)

    networks_count: dict[str, int] = {}
    offers_count: dict[str, int] = {}
    global_count = 0

    for entry in store.suppressions.values():
        if entry.global_:
            global_count += 1
        for nid in entry.networks:
            networks_count[nid] = networks_count.get(nid, 0) + 1
        for oid in entry.offers:
            offers_count[oid] = offers_count.get(oid, 0) + 1

    nets = []
    for n in (store.networks or {}).values():
        count = networks_count.get(n.id, 0)
        if count > 0:
            nets.append({"id": n.id, "name": n.name, "unsubscribers": count})

    offs = []
    for o in (store.offers or {}).values():
        count = offers_count.get(o.id, 0)
        if count > 0:
            offs.append({"id": o.id, "name": o.name, "unsubscribers": count})

    return {"networks": nets, "offers": offs, "global_count": global_count}


# ── Unsubscribers listing ──

def get_unsubscribers_for_target(
    fernet: Fernet,
    level: str,
    target: str,
    since: int = 0,
) -> list[dict]:
    with _lock:
        store = _load(fernet)
        results = []
        for email_hash, entry in store.suppressions.items():
            ts = None
            if level == "global" and entry.global_:
                ts = entry.global_
            elif level == "network":
                ts = entry.networks.get(target)
            elif level == "offer":
                ts = entry.offers.get(target)
            if ts is not None and ts > since:
                results.append({
                    "email_hash": email_hash,
                    "email": entry.email,
                    "md5": entry.md5,
                    "timestamp": ts,
                })
    results.sort(key=lambda r: r["timestamp"], reverse=True)
    return results


def get_all_statistics(fernet: Fernet) -> dict:
    with _lock:
        store = _load(fernet)

    total_suppressed = len(store.suppressions)
    global_count = 0
    network_counts: dict[str, int] = {}
    offer_counts: dict[str, int] = {}
    total_network = 0
    total_offer = 0

    for entry in store.suppressions.values():
        if entry.global_:
            global_count += 1
        for nid in entry.networks:
            network_counts[nid] = network_counts.get(nid, 0) + 1
            total_network += 1
        for oid in entry.offers:
            offer_counts[oid] = offer_counts.get(oid, 0) + 1
            total_offer += 1

    net_details = []
    for n in (store.networks or {}).values():
        c = network_counts.get(n.id, 0)
        net_details.append({"id": n.id, "name": n.name, "count": c})

    off_details = []
    for o in (store.offers or {}).values():
        c = offer_counts.get(o.id, 0)
        net_name = ""
        net = (store.networks or {}).get(o.network_id)
        if net:
            net_name = net.name
        off_details.append({"id": o.id, "name": o.name, "network": net_name, "count": c})

    return {
        "total_suppressed": total_suppressed,
        "global": {"count": global_count},
        "networks": {"total": total_network, "details": net_details},
        "offers": {"total": total_offer, "details": off_details},
    }


# ── Feed token management ──

def get_unsub_token(fernet: Fernet, level: str, target: str) -> str:
    with _lock:
        store = _load(fernet)
        if level == "network":
            net = (store.networks or {}).get(target)
            return net.unsub_token if net else ""
        elif level == "offer":
            off = (store.offers or {}).get(target)
            return off.unsub_token if off else ""
    return ""


def generate_unsub_token(fernet: Fernet, level: str, target: str) -> str:
    existing = get_unsub_token(fernet, level, target)
    if existing:
        return existing
    return regenerate_unsub_token(fernet, level, target)


def regenerate_unsub_token(fernet: Fernet, level: str, target: str) -> str:
    import secrets
    from .crypto import sign_unsubscribe_token
    secret = os.environ["SECRET_KEY"]
    token = sign_unsubscribe_token(secret, level, target)
    with _lock:
        store = _load(fernet)
        if level == "network":
            net = (store.networks or {}).get(target)
            if not net:
                raise ValueError("Network not found")
            net.unsub_token = token
        elif level == "offer":
            off = (store.offers or {}).get(target)
            if not off:
                raise ValueError("Offer not found")
            off.unsub_token = token
        else:
            raise ValueError("Invalid level")
        _save(fernet, store)
    return token


def get_feed_token(fernet: Fernet, level: str, target: str) -> str:
    with _lock:
        store = _load(fernet)
        if level == "network":
            net = (store.networks or {}).get(target)
            return net.feed_token if net else ""
        elif level == "offer":
            off = (store.offers or {}).get(target)
            return off.feed_token if off else ""
    return ""


def generate_feed_token(fernet: Fernet, level: str, target: str) -> str:
    existing = get_feed_token(fernet, level, target)
    if existing:
        return existing
    return regenerate_feed_token(fernet, level, target)


def regenerate_feed_token(fernet: Fernet, level: str, target: str) -> str:
    import secrets
    token = secrets.token_hex(24)
    with _lock:
        store = _load(fernet)
        if level == "network":
            net = (store.networks or {}).get(target)
            if not net:
                raise ValueError("Network not found")
            net.feed_token = token
        elif level == "offer":
            off = (store.offers or {}).get(target)
            if not off:
                raise ValueError("Offer not found")
            off.feed_token = token
        else:
            raise ValueError("Invalid level")
        _save(fernet, store)
    return token


def get_offer_unsubscribers_list(fernet: Fernet, offer_id: str) -> list[dict]:
    with _lock:
        store = _load(fernet)
        off = (store.offers or {}).get(offer_id)
        if not off:
            return []
        return list(off.unsubscribers)


def get_offer_csv_data(fernet: Fernet, offer_id: str, format: str = "plain", since: int = 0) -> str:
    records = get_offer_unsubscribers_list(fernet, offer_id)
    if since:
        records = [r for r in records if r.get("timestamp", 0) > since]
    lines = []
    for r in records:
        val = r.get("md5" if format == "md5" else "email", "")
        if val:
            lines.append(val)
    return "\n".join(lines) + ("\n" if lines else "")


def get_offer_statistics(fernet: Fernet, offer_id: str) -> dict:
    records = get_offer_unsubscribers_list(fernet, offer_id)
    total = len(records)
    tlds: dict[str, int] = {}
    for r in records:
        email = r.get("email", "")
        if "@" in email:
            domain = email.split("@", 1)[1].lower()
            tlds[domain] = tlds.get(domain, 0) + 1
    sorted_tlds = sorted(tlds.items(), key=lambda x: -x[1])
    return {
        "total": total,
        "tlds": [{"domain": d, "count": c} for d, c in sorted_tlds],
    }


def get_offers_summary(fernet: Fernet) -> list[dict]:
    with _lock:
        store = _load(fernet)

    networks = {n.id: n.name for n in (store.networks or {}).values()}

    offer_counts: dict[str, int] = {}
    offer_last_ts: dict[str, int] = {}

    for entry in store.suppressions.values():
        for oid, ts in entry.offers.items():
            offer_counts[oid] = offer_counts.get(oid, 0) + 1
            if ts > offer_last_ts.get(oid, 0):
                offer_last_ts[oid] = ts

    results = []
    for o in (store.offers or {}).values():
        results.append({
            "id": o.id,
            "name": o.name,
            "network_id": o.network_id,
            "network_name": networks.get(o.network_id, ""),
            "count": offer_counts.get(o.id, 0),
            "last_unsubscribed": offer_last_ts.get(o.id, 0),
        })

    results.sort(key=lambda r: r["count"], reverse=True)
    return results


def get_offer_csv_data_by_tld(fernet: Fernet, offer_id: str, domain: str, format: str = "plain") -> str:
    records = get_offer_unsubscribers_list(fernet, offer_id)
    lines = []
    for r in records:
        email = r.get("email", "")
        if "@" in email and email.split("@", 1)[1].lower() == domain.lower():
            val = r.get("md5" if format == "md5" else "email", "")
            if val:
                lines.append(val)
    return "\n".join(lines) + ("\n" if lines else "")
