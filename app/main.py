import os

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse, RedirectResponse

from .routes.unsubscribe import router as unsubscribe_router
from .routes.status import router as status_router
from .routes.admin import router as admin_router
from .routes.auth import router as auth_router
from .crypto import make_fernet
from .store import user_count
from .middleware import add_middleware

app = FastAPI(
    title="Suppression Manager",
    description="Stateless opt-out and suppression manager",
    version="2.0.0",
)

add_middleware(app)

app.include_router(unsubscribe_router)
app.include_router(status_router)
app.include_router(admin_router)
app.include_router(auth_router)


@app.get("/")
def root():
    fernet = make_fernet(os.environ["SECRET_KEY"])
    if user_count(fernet) == 0:
        return RedirectResponse(url="/auth/setup")
    return RedirectResponse(url="/auth/login")


@app.get("/health")
def health():
    return {"status": "ok"}
