from fastapi import APIRouter, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

from app.database.database import get_db

from app.database import crud, models

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

# HOME PAGE
@router.get("/")
def home(request: Request, db: Session = Depends(get_db)):
    notes = crud.get_notes(db)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "notes": notes
    })

# ADD NOTE
@router.post("/add-note")
def add_note(note: str = Form(...), db: Session = Depends(get_db)):
    crud.create_note(db, note)
    return RedirectResponse("/", status_code=303)

# DELETE
@router.get("/delete-note/{note_id}")
def delete_note(note_id: int, db: Session = Depends(get_db)):
    crud.delete_note(db, note_id)
    return RedirectResponse("/", status_code=303)

# EDIT PAGE
@router.get("/edit/{note_id}")
def edit_page(note_id: int, request: Request, db: Session = Depends(get_db)):
    note = db.query(models.Note).filter(models.Note.id == note_id).first()
    return templates.TemplateResponse("edit.html", {
        "request": request,
        "note": note.text,
        "note_id": note_id
    })

# SAVE EDIT
@router.post("/edit/{note_id}")
def update_note(note_id: int, note: str = Form(...), db: Session = Depends(get_db)):
    crud.update_note(db, note_id, note)
    return RedirectResponse("/", status_code=303)
