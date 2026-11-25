from uuid import UUID
from app.Models.document import DocumentResponse


class DocumentRepository:
    def __init__(self):
        self._documents: dict[UUID, DocumentResponse] = {}