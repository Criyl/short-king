from fastapi import FastAPI, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse,FileResponse
from pydantic import BaseModel
from server.models import UrlLookup, generate_url, url_repository
from bson import ObjectId
from typing import Annotated

app: FastAPI = FastAPI()
app.mount("/public", StaticFiles(directory="public"),name="public")

@app.post("/create")
def create(url: Annotated[str, Form()]) -> UrlLookup:
    existing = url_repository.find_one_by({"url": url})
    if existing is None:
        generated = generate_url(url)
        return generated
        
    return existing

@app.get("/{short_url}")
def redirect(short_url: str ) -> str:
    redirect_url = url_repository.find_one_by({"salt": short_url})
    print(redirect_url)
    return RedirectResponse(redirect_url.url)

@app.get("/")
def index() -> FileResponse:
    return FileResponse('public/index.html')