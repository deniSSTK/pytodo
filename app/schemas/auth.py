from pydantic import BaseModel


class AuthUser(BaseModel):
    id: str
    access_token: str

class AuthToken(BaseModel):
    access_token: str