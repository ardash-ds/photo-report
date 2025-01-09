import os

from pptx import Presentation
from pptx.util import Inches

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


app = FastAPI()
templates = Jinja2Templates(directory="templates")
directory = "static/photo"
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/") #, response_class=HTMLResponse)
async def read_item(request: Request):
    files = os.listdir(directory)
    print(files)
    return templates.TemplateResponse(request=request, name="photo_resport.html", context={"files": files})

