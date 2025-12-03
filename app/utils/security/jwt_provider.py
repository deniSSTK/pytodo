import jwt
from datetime import datetime, timedelta
from typing import Dict, Optional

from core.config import Settings
from schemas.auth import AuthUser

ALGORITHM = "HS256"
ACCESS_EXPIRE_MINUTES = 15
REFRESH_EXPIRE_DAYS = 7

class JWTProvider:
    def __init__(self, algorithm: str = ALGORITHM):
        self.secret_key = Settings.JWT_SECRET_KEY
        self.algorithm = algorithm

    def _create_token(self, data: Dict, token_type: str, expires_delta: Optional[timedelta] = None) -> str:
        to_encode = data.copy()
        if expires_delta is None:
            if token_type == "access":
                expires_delta = timedelta(minutes=ACCESS_EXPIRE_MINUTES)
            elif token_type == "refresh":
                expires_delta = timedelta(days=REFRESH_EXPIRE_DAYS)
        expire = datetime.utcnow() + expires_delta
        to_encode.update({"exp": expire, "type": token_type})
        return jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)

    def create_access_token(self, user: AuthUser, expires_delta: Optional[timedelta] = None) -> str:
        data = user.model_dump(exclude_unset=True)
        return self._create_token(data, token_type="access", expires_delta=expires_delta)

    def create_refresh_token(self, user: AuthUser, expires_delta: Optional[timedelta] = None) -> str:
        data = user.model_dump(exclude_unset=True)
        return self._create_token(data, token_type="refresh", expires_delta=expires_delta)

    def decode_token(self, token: str) -> Dict:
        try:
            return jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
        except jwt.ExpiredSignatureError:
            raise Exception("Token expired")
        except jwt.InvalidTokenError:
            raise Exception("Invalid token")

jwt_provider = JWTProvider()