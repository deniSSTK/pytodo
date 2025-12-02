from pydantic import BaseModel


class AuthUser(BaseModel):
    id: str
    access_token: str