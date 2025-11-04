from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.src.database.base import Base


class AccessGroup(Base):
    __tablename__ = "access_groups"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)

    # Relationship
    users = relationship("User", back_populates="group")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)  # This should be hashed
    group_id = Column(Integer, ForeignKey("access_groups.id"), nullable=True)

    # Relationship
    group = relationship("AccessGroup", back_populates="users")