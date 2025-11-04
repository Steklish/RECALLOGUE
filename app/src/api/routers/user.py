from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.src.database.session import get_db
from app.src.services import user_service
from app.src.schema import UserCreate, UserUpdate, UserInDB

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserInDB)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user.
    """
    # TODO: Implement user creation logic
    pass


@router.get("/{user_id}", response_model=UserInDB)
def get_user(user_id: int, db: Session = Depends(get_db)):
    """
    Get a user by ID.
    """
    # TODO: Implement get user by ID logic
    pass


@router.get("/", response_model=List[UserInDB])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Get a list of users with pagination.
    """
    # TODO: Implement get all users logic
    pass


@router.put("/{user_id}", response_model=UserInDB)
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    """
    Update a user by ID.
    """
    # TODO: Implement update user logic
    pass


@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    """
    Delete a user by ID.
    """
    # TODO: Implement delete user logic
    pass


@router.get("/username/{username}", response_model=UserInDB)
def get_user_by_username(username: str, db: Session = Depends(get_db)):
    """
    Get a user by username.
    """
    # TODO: Implement get user by username logic
    pass