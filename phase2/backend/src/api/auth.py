from fastapi import APIRouter, HTTPException, status, Depends
from typing import Optional
from datetime import timedelta
from pydantic import BaseModel

from ..auth.jwt_validator import create_access_token
from ..logging_config import logger
from ..models.user import UserCreate, User
from ..database.session import get_session
from sqlmodel import Session, select

router = APIRouter()

# Simple in-memory user store for demo purposes
# In production, this would be a database
demo_users = {
    "user@example.com": {
        "id": 1,
        "email": "user@example.com",
        "name": "Demo User",
        "hashed_password": "dummy_hashed_password",  # In real app, use proper hashing
        "disabled": False
    },
    "admin@example.com": {
        "id": 2,
        "email": "admin@example.com",
        "name": "Admin User",
        "hashed_password": "dummy_hashed_password",
        "disabled": False
    }
}

# Request models
class LoginRequest(BaseModel):
    email: str
    password: str

class RegisterRequest(BaseModel):
    email: str
    password: str
    name: str


@router.post("/auth/login")
async def login(request: LoginRequest, db: Session = Depends(get_session)):
    """Login endpoint that returns JWT token"""
    email = request.email
    password = request.password

    # In a real app, you'd verify the password properly
    # For demo purposes, we'll just check if email exists
    user = demo_users.get(email)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
        )

    # Ensure the user exists in the database as well to satisfy foreign key constraints
    db_user = db.exec(select(User).where(User.email == email)).first()
    if not db_user:
        # Create user in database if they exist in memory but not in DB
        db_user = User(
            id=user["id"],
            email=user["email"],
            name=user["name"]
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        logger.info(f"Created database record for user {email}")

    # Create JWT token with user info
    access_token_expires = timedelta(minutes=30)
    token_data = {
        "sub": str(user["id"]),
        "email": user["email"],
        "name": user["name"]
    }
    access_token = create_access_token(
        data=token_data, expires_delta=access_token_expires
    )

    logger.info(f"User {user['email']} logged in successfully")

    return {
        "token": access_token,
        "user": {
            "id": user["id"],
            "email": user["email"],
            "name": user["name"]
        },
        "token_type": "bearer"
    }


@router.post("/auth/register")
async def register(request: RegisterRequest, db: Session = Depends(get_session)):
    """Register endpoint that creates user and returns JWT token"""
    email = request.email
    password = request.password
    name = request.name

    # Check if user already exists in the in-memory store
    if email in demo_users:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already registered"
        )

    # Check if user already exists in the database
    existing_user = db.exec(select(User).where(User.email == email)).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already registered"
        )

    # Create new user (in demo, we'll just add to in-memory store)
    new_user_id = max([user["id"] for user in demo_users.values()], default=0) + 1
    new_user = {
        "id": new_user_id,
        "email": email,
        "name": name,
        "hashed_password": "dummy_hashed_password",  # In real app, properly hash
        "disabled": False
    }

    demo_users[email] = new_user

    # Create user in the database as well to satisfy foreign key constraints
    db_user = User(
        id=new_user_id,
        email=email,
        name=name
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    # Create JWT token
    access_token_expires = timedelta(minutes=30)
    token_data = {
        "sub": str(new_user["id"]),
        "email": new_user["email"],
        "name": new_user["name"]
    }
    access_token = create_access_token(
        data=token_data, expires_delta=access_token_expires
    )

    logger.info(f"User {email} registered successfully")

    return {
        "token": access_token,
        "user": {
            "id": new_user["id"],
            "email": new_user["email"],
            "name": new_user["name"]
        },
        "token_type": "bearer"
    }