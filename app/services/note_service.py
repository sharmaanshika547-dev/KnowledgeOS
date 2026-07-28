from sqlalchemy.orm import Session

from app.models.note import Note
from app.repositories.note_repository import note_repository
from app.schemas.note import NoteCreate, NoteUpdate


class NoteService:

    def create_note(
        self,
        db: Session,
        note_data: NoteCreate,
        user_id: int,
    ) -> Note:

        return note_repository.create_note(
            db=db,
            note_data=note_data,
            user_id=user_id,
        )

    def get_note_by_id(
        self,
        db: Session,
        note_id: int,
    ) -> Note:

        note = note_repository.get_note_by_id(
            db=db,
            note_id=note_id,
        )

        if note is None:
            raise ValueError("Note not found")

        return note

    def get_all_notes(
        self,
        db: Session,
    ) -> list[Note]:

        return note_repository.get_all_notes(db=db)

    def update_note(
        self,
        db: Session,
        note_id: int,
        note_data: NoteUpdate,
    ) -> Note:

        note = self.get_note_by_id(
            db=db,
            note_id=note_id,
        )

        return note_repository.update_note(
            db=db,
            note_model=note,
            note_data=note_data,
        )

    def delete_note(
        self,
        db: Session,
        note_id: int,
    ) -> None:

        note = self.get_note_by_id(
            db=db,
            note_id=note_id,
        )

        note_repository.delete_note(
            db=db,
            note_model=note,
        )


note_service = NoteService()
