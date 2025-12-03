from pydantic import BaseModel

from schemas.auth import AuthUser


class AuthResponse(BaseModel):
    user: AuthUser
    access_token: str

    # class Config:
    #     orm_mode = True
