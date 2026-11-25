from fastapi import APIRouter
from app.services import document_service

router = APIRouter(prefix = "/documents", tags = ["Documents"])

@router.get("/")
def get_documents():
    return document_service.list_documents()

@router.post("/")
def post_documents():
    return document_service.create_document()