from fastapi import FastAPI , Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Mount static files

app.mount("/static:", StaticFiles(directory= "app/static"), name = "Static")

#templates

templates = Jinja2Templates(directory="app/templates")





#in-memory storage for demonstration purposes

notes = []

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "notes" : notes})


@app.post("/add-note")
async def add_note(note:str  = Form(...)):
    notes.append(note)
    return {"message": "Note added successfully", "note": note}