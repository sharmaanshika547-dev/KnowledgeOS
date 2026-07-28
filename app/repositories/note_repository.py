from sqlalchemy.orm import Session

from app.models.note import Note
from app.schemas.note import NoteCreate, NoteUpdate


class NoteRepository:

    def create_note(
        self,
        db: Session,
        note_data: NoteCreate,
        user_id: int,
    ) -> Note:

        note_model = Note(
            title=note_data.title,
            content=note_data.content,
            user_id=user_id,
        )

        db.add(note_model)
        db.commit()
        db.refresh(note_model)

        return note_model

    def get_note_by_id(
        self,
        db: Session,
        note_id: int,
    ) -> Note | None:

        return (
            db.query(Note)
            .filter(Note.id == note_id)
            .first()
        )

    def get_all_notes(
        self,
        db: Session,
    ) -> list[Note]:

        return db.query(Note).all()

    def update_note(
        self,
        db: Session,
        note_model: Note,
        note_data: NoteUpdate,
    ) -> Note:

        note_model.title = note_data.title
        note_model.content = note_data.content

        db.commit()
        db.refresh(note_model)

        return note_model

    def delete_note(
        self,
        db: Session,
        note_model: Note,
    ) -> None:

        db.delete(note_model)
        db.commit()


note_repository = NoteRepository()
