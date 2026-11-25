from fastapi import FastAPI
from routers import documents

app = FastAPI(titlw = "AI Knowledge Assistant")

app.include_router(documents.router)