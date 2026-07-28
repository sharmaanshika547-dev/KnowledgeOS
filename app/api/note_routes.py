from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.schemas.note import NoteCreate, NoteUpdate, NoteResponse
from app.services.note_service import note_service


router = APIRouter(
    prefix="/notes",
    tags=["Notes"],
)


@router.post(
    "/",
    response_model=NoteResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_note(
    note: NoteCreate,
    db: Session = Depends(get_db),
):

    return note_service.create_note(
        db=db,
        note_data=note,
        user_id=1,
    )


@router.get(
    "/",
    response_model=list[NoteResponse],
)
def get_all_notes(
    db: Session = Depends(get_db),
):

    return note_service.get_all_notes(db=db)


@router.get(
    "/{note_id}",
    response_model=NoteResponse,
)
def get_note(
    note_id: int,
    db: Session = Depends(get_db),
):

    try:
        return note_service.get_note_by_id(
            db=db,
            note_id=note_id,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )


@router.put(
    "/{note_id}",
    response_model=NoteResponse,
)
def update_note(
    note_id: int,
    note: NoteUpdate,
    db: Session = Depends(get_db),
):

    try:
        return note_service.update_note(
            db=db,
            note_id=note_id,
            note_data=note,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )


@router.delete(
    "/{note_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_note(
    note_id: int,
    db: Session = Depends(get_db),
):

    try:
        note_service.delete_note(
            db=db,
            note_id=note_id,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )
