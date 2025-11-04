from typing import Optional, List
from sqlalchemy.orm import Session
from app.src.models import User, AccessGroup
from app.src.schema import (
    UserCreate, 
    UserUpdate, 
    UserInDB,
    AccessGroupCreate, 
    AccessGroupUpdate, 
    AccessGroupInDB
)
from app.src.repositories import user_repo, access_group_repo
from app.src.utils.security import get_password_hash


class AccessGroupService:
    def create_access_group(self, db: Session, access_group_in: AccessGroupCreate) -> AccessGroupInDB:
        db_access_group = access_group_repo.create(db, obj_in=access_group_in)
        return AccessGroupInDB.model_validate(db_access_group)

    def get_access_group(self, db: Session, access_group_id: int) -> Optional[AccessGroupInDB]:
        db_access_group = access_group_repo.get(db, id=access_group_id)
        if db_access_group:
            return AccessGroupInDB.model_validate(db_access_group)
        return None

    def get_access_group_by_name(self, db: Session, name: str) -> Optional[AccessGroupInDB]:
        db_access_group = access_group_repo.get_by_name(db, name=name)
        if db_access_group:
            return AccessGroupInDB.model_validate(db_access_group)
        return None

    def get_access_groups(self, db: Session, skip: int = 0, limit: int = 100) -> List[AccessGroupInDB]:
        db_access_groups = access_group_repo.get_all(db, skip=skip, limit=limit)
        return [AccessGroupInDB.model_validate(ag) for ag in db_access_groups]

    def update_access_group(self, db: Session, access_group_id: int, 
                           access_group_in: AccessGroupUpdate) -> Optional[AccessGroupInDB]:
        db_access_group = access_group_repo.get(db, id=access_group_id)
        if not db_access_group:
            return None
        updated_access_group = access_group_repo.update(db, db_obj=db_access_group, obj_in=access_group_in)
        return AccessGroupInDB.model_validate(updated_access_group)

    def delete_access_group(self, db: Session, access_group_id: int) -> bool:
        db_access_group = access_group_repo.get(db, id=access_group_id)
        if not db_access_group:
            return False
        db.delete(db_access_group)
        db.commit()
        return True


class UserService:
    def create_user(self, db: Session, user_in: UserCreate) -> UserInDB:
        # Hash the password before storing
        hashed_password = get_password_hash(user_in.password)
        user_in_db = user_in.model_copy(update={"password": hashed_password})
        db_user = user_repo.create(db, obj_in=user_in_db)
        return UserInDB.model_validate(db_user)

    def get_user(self, db: Session, user_id: int) -> Optional[UserInDB]:
        db_user = user_repo.get(db, id=user_id)
        if db_user:
            return UserInDB.model_validate(db_user)
        return None

    def get_user_by_username(self, db: Session, username: str) -> Optional[UserInDB]:
        db_user = user_repo.get_by_username(db, username=username)
        if db_user:
            return UserInDB.model_validate(db_user)
        return None

    def get_users(self, db: Session, skip: int = 0, limit: int = 100) -> List[UserInDB]:
        db_users = user_repo.get_all(db, skip=skip, limit=limit)
        return [UserInDB.model_validate(user) for user in db_users]

    def update_user(self, db: Session, user_id: int, user_in: UserUpdate) -> Optional[UserInDB]:
        db_user = user_repo.get(db, id=user_id)
        if not db_user:
            return None
        updated_user = user_repo.update(db, db_obj=db_user, obj_in=user_in)
        return UserInDB.model_validate(updated_user)

    def delete_user(self, db: Session, user_id: int) -> bool:
        db_user = user_repo.get(db, id=user_id)
        if not db_user:
            return False
        db.delete(db_user)
        db.commit()
        return True


# Create instances of the services
user_service = UserService()
access_group_service = AccessGroupService()