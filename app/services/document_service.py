from app.Models import document, DocumentResponse
from uuid import uuid4

def create_document(request):
    document = DocumentResponse(
        id=uuid4(),
        name=request.name,
        content=request.content)
    return document