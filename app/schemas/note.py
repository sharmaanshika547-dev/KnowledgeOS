from pydantic import BaseModel, Field
from typing import Optional


# ── Request Models ─────────────────────────────────────────────

class NoteCreate(BaseModel):
    title: str = Field(
        ...,
        min_length=1,
        max_length=255,
        description="The title of the note"
    )
    content: str = Field(
        default="",
        description="The body of the note"
    )


class NoteUpdate(BaseModel):
    title: Optional[str] = Field(
        default=None,
        min_length=1,
        max_length=255
    )
    content: Optional[str] = Field(
        default=None
    )


# ── Response Models ────────────────────────────────────────────

class NoteResponse(BaseModel):
    id: int
    title: str
    content: str

    class Config:
        from_attributes = True
