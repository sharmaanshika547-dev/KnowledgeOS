from sqlalchemy.orm import Session
from app.database.db import get_db
from fastapi import APIRouter, HTTPException,Depends
from typing import List
from app.models.note import Note

from app.schemas.note import (
    NoteCreate,
    NoteUpdate,
    NoteResponse
)

router = APIRouter(
    prefix="/notes",
    tags=["Notes"]
)


@router.get("/", response_model=List[NoteResponse])
def get_all_notes(
     db: Session = Depends(get_db)
):
     return db.query(Note).all()
     return notes
@router.post("/", response_model=NoteResponse, status_code=201)
def create_note(note: NoteCreate,
    db:session = Depends(get_db):
    

    new_note = Note(
        title: note.title,
        content: note.content
    )

    db.add(new_note)
    db.commit()
    db.refresh(new_note)
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
