from pydantic import BaseModel, Field
from typing import Optional


class UserEntry(BaseModel):
    email: str
    password_hash: str
    role: str = "user"
    api_key: str = ""
    created_at: int = 0


class SuppressionEntry(BaseModel):
    global_: bool = Field(default=False, alias="global")
    networks: dict[str, int] = Field(default_factory=dict)
    offers: dict[str, int] = Field(default_factory=dict)
    history: list[dict] = Field(default_factory=list)

    model_config = {"populate_by_name": True, "extra": "allow"}


class SuppressionStore(BaseModel):
    version: int = 2
    users: dict[str, UserEntry] = Field(default_factory=dict)
    suppressions: dict[str, SuppressionEntry] = Field(default_factory=dict)


class GenerateLinkRequest(BaseModel):
    email: Optional[str] = None
    level: str = Field(pattern=r"^(global|network|offer)$")
    network_id: Optional[str] = None
    network_name: Optional[str] = None
    offer_id: Optional[str] = None
    offer_name: Optional[str] = None


class GenerateLinkResponse(BaseModel):
    unsubscribe_url: str
    token: str


class UnsubscribeFormRequest(BaseModel):
    token: str
    email: str


class CheckRequest(BaseModel):
    h: str
    network: Optional[str] = None
    offer: Optional[str] = None


class CheckResponse(BaseModel):
    allowed: bool


class StatusResponse(BaseModel):
    email_hash: str
    suppressed: bool
    global_suppressed: bool = False
    network_suppressions: list[str] = []
    offer_suppressions: list[str] = []


class SetupRequest(BaseModel):
    email: str
    password: str = Field(min_length=8)


class LoginRequest(BaseModel):
    email: str
    password: str


class LoginResponse(BaseModel):
    token: str
    email: str
    role: str


class CreateUserRequest(BaseModel):
    email: str
    password: str = Field(min_length=8)
    role: str = Field(default="user", pattern=r"^(admin|user)$")


class UserResponse(BaseModel):
    email: str
    role: str
    api_key: str
    created_at: int
