from pydantic import BaseModel, Field, ConfigDict
from uuid import UUID, uuid4

class Document(BaseModel, str_strip_whitespace=True):
    name: str = Field(min_length=1, max_length=200)
    content: str = Field(min_length=1)

class DocumentResponse(Document):
    id: UUID = Field(default_factory=uuid4)
