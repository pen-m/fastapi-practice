from fastapi import HTTPException, status, Depends, Header
from fastapi.security import OAuth2PasswordBearer
from typing import Optional

TOKENS = {}

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")


# not secure, just for testing in fastapi
def generate_token(user_id: str) -> str:
    token = f"token-{user_id}"
    TOKENS[token] = user_id
    return token


# def get_current_user(token: str = Depends(oauth2_scheme)) -> str:
#     user_id = TOKENS.get(token)
#     if not user_id:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid authentication credentials",
#         )
#     return user_id

#temporary for testing truncated workflow
def get_current_user(authorization: str = Header(...)) -> str:
    token = authorization.replace("Bearer ", "")
    user_id = TOKENS.get(token)
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    return user_id