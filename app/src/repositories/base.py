from typing import Any, Generic, Type, TypeVar
from sqlalchemy.orm import Session, DeclarativeMeta
from pydantic import BaseModel

# SQLAlchemy Base class definition
from sqlalchemy.orm import declarative_base
Base = declarative_base()

ModelType = TypeVar("ModelType", bound=DeclarativeMeta)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)

class BaseRepository(Generic[ModelType, CreateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get(self, db: Session, id: Any) -> ModelType | None:
        return db.query(self.model).filter(self.model.id == id).first() # type: ignore

    def get_all(self, db: Session, *, skip: int = 0, limit: int = 100) -> list[ModelType]:
        return db.query(self.model).offset(skip).limit(limit).all()

    def create(self, db: Session, *, obj_in: CreateSchemaType) -> ModelType:
        db_obj = self.model(**obj_in.model_dump()) # type: ignore
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj