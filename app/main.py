from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.routers import notes

app = FastAPI()

# Correct static mount
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Templates setup
templates = Jinja2Templates(directory="app/templates")

# REGISTER ROUTER HERE
app.include_router(notes.router)
