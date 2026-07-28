from pydantic import BaseModel,ConfigDict


class NoteCreate(BaseModel):
    title: str
    content: str


class NoteUpdate(BaseModel):
    title: str
    content: str


class NoteResponse(BaseModel):
    id: int
    title: str
    content: str
    user_id: int

model_config = ConfigDict(from_attributes=True)

