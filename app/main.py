from fastapi import FastAPI

from app.api.note_routes import router as note_router
from app.database.db import Base, engine

import app.models.note
import app.models.user


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(note_router)
