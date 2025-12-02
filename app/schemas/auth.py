from pydantic import BaseModel


class AuthUser(BaseModel):
    id: str

class AuthToken(BaseModel):
    access_token: str