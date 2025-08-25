from fastapi import APIRouter, HTTPException, status, Depends
from app.models.user import UserIn, UserOut
from app.models.common import Timestamps, WithID
from app.core.auth import get_current_user, generate_token
from typing import Dict
from uuid import uuid4
from datetime import datetime

router = APIRouter()

_USER_DB: Dict[str, UserOut] = {}


# create user
@router.post("/create", response_model=UserOut, status_code=201)
def create_user(user: UserIn):
    new_user = UserOut(**user.model_dump())
    _USER_DB[new_user.id] = new_user
    return new_user


# login route
@router.post("/login")
def login_user(email: str):
    # placeholder code for now, replace with proper auth eventually
    for user in _USER_DB.values():
        if user.email == email:
            token = generate_token(user.id)
            return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=404, detail="User not found")


# get user profile
@router.get("/me", response_model=UserOut)
def get_user_profile(current_user_id: str = Depends(get_current_user)):
    user = _USER_DB.get(current_user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
