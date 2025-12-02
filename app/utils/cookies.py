from fastapi import Response, Request
from typing import Optional

COOKIE_REFRESH = "refresh_token"

def set_cookie(response: Response, key: str, value: str, max_age: int = 3600, httponly: bool = True):
    response.set_cookie(
        key=key,
        value=value,
        max_age=max_age,
        httponly=httponly,
        samesite="lax",
        secure=False
    )

def get_cookie(request: Request, key: str) -> Optional[str]:
    return request.cookies.get(key)

def delete_cookie(response: Response, key: str):
    response.delete_cookie(key)
