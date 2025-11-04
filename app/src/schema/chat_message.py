from  pydantic import BaseModel, Field
from typing import List

class Message(BaseModel):
    user_id : int = Field(description="User id")
    owner : str = Field(description="Owner of the message (user / app)")
    content : str = Field(description="Message contents")
    attr : dict = Field(description="Additional attributes")
    thread_id : int = Field(description="Related thread ID")
    sources_documents : List[int] = Field(description="List of related chunk IDs")
    sources_other : List[str] = Field(description="List of related sources links")
    raw : str = Field(description="Any raw retrieved data related to the message")
    