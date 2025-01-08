from pptx import Presentation
from pptx.util import Inches

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("") #, response_class=HTMLResponse)
async def read_item(request: Request, item_id: int):
    return templates.TemplateResponse("photo_resport.html", {})

