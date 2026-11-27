from fastapi import FastAPI
from routers import documents

app = FastAPI(title = "AI Knowledge Assistant")

app.include_router(documents.router)
