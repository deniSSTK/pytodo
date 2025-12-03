from fastapi import Request, HTTPException

from services.auth import auth_service


async def auth_required(request: Request):
    token = request.headers.get("Authorization")

    if not token:
        raise HTTPException(status_code=401, detail="Unauthorized")

    token = token.replace("Bearer ", "")
    auth_user = await auth_service.get_user_from_token(token)

    request.state.auth_user = auth_user

    return auth_user
