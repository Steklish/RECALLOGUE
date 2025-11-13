from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from .chat_message import ChatMessage

class ThreadBase(BaseModel):
    name: str
    allowed_sources: Optional[List[str]] = None  # Corresponds to nullable=True

class ThreadCreate(ThreadBase):
    pass

class ThreadUpdate(BaseModel):
    name: Optional[str] = None
    allowed_sources: Optional[List[str]] = None


class Thread(ThreadBase):
    id: int
    created_at: datetime
    updated_at: datetime
    messages: Optional[List[ChatMessage]] = None

    class Config:
        from_attributes = True