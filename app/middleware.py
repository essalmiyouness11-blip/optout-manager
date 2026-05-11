import os
import time

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware


# Host routing rules: (host_prefix, allowed_path_prefixes) — only requests to these
# subdomains are restricted to their allowed paths. Unknown hosts = unrestricted.
HOST_ROUTES = [
    ("dlx.", ["/feed", "/health"]),
    ("optout.", ["/u", "/check", "/status", "/health"]),
    ("unsubmepanel.", ["/admin", "/auth", "/health"]),
]


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
