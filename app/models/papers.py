from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Text
from uuid import UUID, uuid4


class Paper(BaseModel):
    id: Optional[UUID] = uuid4()
    title: str
    abstract: Optional[Text] = None
    authors: list[str]
    categories: list[str]
    created_at: datetime = datetime.now()
    published: bool = False
