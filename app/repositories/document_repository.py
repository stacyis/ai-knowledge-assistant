from uuid import UUID
from app.Models.document import DocumentResponse


class DocumentRepository:
    def __init__(self):
        self._documents: dict[UUID, DocumentResponse] = {}

    def add(self, document: DocumentResponse) -> str:
        self._documents[document.id] = document
        return f"Добавлен документ: {document.name}"
    
    def get_all(self) -> list[DocumentResponse]:
        return self._documents.values()

    def get_by_id(self, document_id: UUID) -> DocumentResponse | None:
        return self._documents.get(document_id)