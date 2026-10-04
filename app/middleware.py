import os
import time
from urllib.parse import urlparse

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware


def _host_of(env_var: str, fallback: str = "") -> str:
    """Extract the hostname from a configured base URL env var."""
    raw = os.environ.get(env_var, fallback)
    host = urlparse(raw).hostname or ""
    return host.lower()


# Host routing rules: (hostname, allowed_path_prefixes) — only requests to these
# subdomains are restricted to their allowed paths. Unknown hosts = unrestricted.
# Derived from the configured base URLs so any domain set in .env just works.
HOST_ROUTES = [
    (_host_of("DOWNLOAD_BASE_URL"), ["/feed", "/health"]),
    (_host_of("UNSUBSCRIBE_BASE_URL"), ["/u", "/check", "/status", "/health"]),
    (_host_of("BASE_URL"), ["/", "/admin", "/auth", "/health"]),
]
HOST_ROUTES = [(h, paths) for h, paths in HOST_ROUTES if h]


class RateLimitMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, max_requests: int = 20, window: int = 60):
        super().__init__(app)
        self.max_requests = max_requests
        self.window = window
        self.clients: dict[str, list[float]] = {}

    async def dispatch(self, request: Request, call_next):
        if request.url.path.startswith(("/u", "/check")):
            ip = request.client.host if request.client else "unknown"
            now = time.time()
            self.clients.setdefault(ip, [])
            self.clients[ip] = [t for t in self.clients[ip] if now - t < self.window]
            if len(self.clients[ip]) >= self.max_requests:
                return JSONResponse(status_code=429, content={"detail": "Rate limit exceeded"})
            self.clients[ip].append(now)

        response = await call_next(request)
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        return response


class HostRoutingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        host = request.headers.get("host", "").lower().split(":")[0]
        path = request.url.path

        # Skip host check for localhost / IP
        if "localhost" in host or host.startswith("127.") or host.startswith("192.") or host.startswith("10."):
            return await call_next(request)

        for prefix, allowed_prefixes in HOST_ROUTES:
            if host.startswith(prefix):
                if not any(path.startswith(p) for p in allowed_prefixes):
                    return JSONResponse(
                        status_code=403,
                        content={"detail": f"Not available on this subdomain"},
                    )
                break

        return await call_next(request)


def add_middleware(app: FastAPI):
    app.add_middleware(RateLimitMiddleware, max_requests=20, window=60)
    app.add_middleware(HostRoutingMiddleware)
