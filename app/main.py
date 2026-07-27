from fastapi import FastAPI
from app.api.note_routes import router as note_router
from app.database.db import Base, engine
from app.models.note import Note
app = FastAPI(
    title="KnowledgeOS API",
    description="Backend API for managing notes and learning resources",
    version="1.0.0"
)
Base.metadata.create_all(bind=engine)

app.include_router(note_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to KnowledgeOS API",
        "status": "running"
    }
