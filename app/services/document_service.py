from app.Models import document, DocumentResponse
from uuid import uuid4
from app.repositories import DocumentRepository

def create_document(request: DocumentResponse, history: DocumentRepository):
    document = DocumentResponse(
        id=uuid4(),
        name=request.name,
        content=request.content)
    history.add(document)
    return document

def list_documents(history: DocumentRepository):
    return history

