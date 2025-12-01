from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse

from app.services.notes_service import notes_list

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


# HOME PAGE
@router.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "notes": notes_list}
    )


# ADD NOTE
@router.post("/add-note")
def add_note(note: str = Form(...)):
    notes_list.append(note)
    return RedirectResponse("/", status_code=303)


# DELETE NOTE
@router.get("/delete-note/{note_id}")
def delete_note(note_id: int):
    if 0 <= note_id < len(notes_list):
        notes_list.pop(note_id)
    return RedirectResponse("/", status_code=303)


# EDIT PAGE
@router.get("/edit/{note_id}")
def edit_page(note_id: int, request: Request):
    return templates.TemplateResponse(
        "edit.html",
        {"request": request, "note_id": note_id, "note": notes_list[note_id]}
    )


# SAVE EDITED NOTE
@router.post("/edit/{note_id}")
def edit_note(note_id: int, note: str = Form(...)):
    notes_list[note_id] = note
    return RedirectResponse("/", status_code=303)
