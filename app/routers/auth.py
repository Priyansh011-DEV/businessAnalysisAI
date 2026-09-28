from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.repositories.user_repository import UserRepository
from app.schema.user import UserRegister, UserLogin, UserResponse, TokenResponse
from app.services.auth_service import AuthService


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register", response_model=UserResponse)
def register(
    user_data: UserRegister,
    db: Session = Depends(get_db)
):
    repository = UserRepository(db)
    service = AuthService(repository)

    try:
        user = service.register(
            username=user_data.username,
            password=user_data.password,
            tenant_id=1
        )

        return user

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
        
@router.post("/login", response_model=TokenResponse)
def login(
    user_data: UserLogin,
    db: Session = Depends(get_db)
):
    repository = UserRepository(db)
    service = AuthService(repository)

    try:
        access_token = service.login(
            username=user_data.username,
            password=user_data.password
        )

        return {
            "access_token": access_token,
            "token_type": "bearer"
        }

    except ValueError as e:
        raise HTTPException(
            status_code=401,
            detail=str(e)
        )