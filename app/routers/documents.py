from fastapi import APIRouter
from app.services import document_service
from app.repositories import DocumentRepository

history = DocumentRepository()
router = APIRouter(prefix = "/documents", tags = ["Documents"])

@router.get("")
def get_documents():
    return document_service.list_documents(history)

@router.post("/")
def post_documents():
    return document_service.create_document(history)