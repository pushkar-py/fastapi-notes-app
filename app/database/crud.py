#this for CRUD operations on Note model like querying, adding,deleting,updating notes

from sqlalchemy.orm import Session
from app.database import models

def get_notes(db: Session):
    return db.query(models.Note).all()

def create_note(db:Session, text : str):
    note = models.Note(text = text)
    db.add(note)
    db.commit()
    db.refresh(note)
    return note

def delete_note(db:Session, note_id: int):
    note = db.query(models.Note).filter(models.Note.id == note_id).first()
    if note:
        db.delete(note)
        db.commit()
    return note

def update_note(db:Session, note_id:int, new_text:str):
    note = db.query(models.Note).filter(models.Note.id == note_id).first()
    if note:
        note.text = new_text
        db.commit()
        db.refresh(note)
    return note