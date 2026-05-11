import os

from fastapi import APIRouter, Depends, Query

from ..crypto import make_fernet
from ..store import get_status
from ..models import StatusResponse

router = APIRouter()


def _get_fernet():
    return make_fernet(os.environ["SECRET_KEY"])


@router.get("/status", response_model=StatusResponse)
def status(h: str = Query(..., description="SHA256 of email")):
    fernet = _get_fernet()
    return StatusResponse(**get_status(fernet, h))
