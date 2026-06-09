from fastapi import APIRouter, HTTPException
from typing import List

from app.schemas.note import (
    NoteCreate,
    NoteUpdate,
    NoteResponse
)

router = APIRouter(
    prefix="/notes",
    tags=["Notes"]
)

# Temporary in-memory storage
notes_db: List[dict] = []
next_id = 1


@router.get("/", response_model=List[NoteResponse])
def get_all_notes():
    """
    Return all notes.
    """
    return notes_db


@router.post("/", response_model=NoteResponse, status_code=201)
def create_note(note: NoteCreate):
    """
    Create a new note.
    """
    global next_id

    new_note = {
        "id": next_id,
        "title": note.title,
        "content": note.content
    }

    notes_db.append(new_note)
    next_id += 1

    return new_note


@router.put("/{note_id}", response_model=NoteResponse)
def update_note(note_id: int, note_data: NoteUpdate):
    """
    Update an existing note.
    """

    for note in notes_db:

        if note["id"] == note_id:

            if note_data.title is not None:
                note["title"] = note_data.title

            if note_data.content is not None:
                note["content"] = note_data.content

            return note

    raise HTTPException(
        status_code=404,
        detail="Note not found"
    )


@router.delete("/{note_id}", status_code=204)
def delete_note(note_id: int):
    """
    Delete a note.
    """

    global notes_db

    original_length = len(notes_db)

    notes_db = [
        note
        for note in notes_db
        if note["id"] != note_id
    ]

    if len(notes_db) == original_length:
        raise HTTPException(
            status_code=404,
            detail="Note not found"
        )

    return
