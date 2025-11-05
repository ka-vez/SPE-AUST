from db.database import engine
from db.models import Base
import endpoints

from fastapi import FastAPI, Depends, status, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.include_router(endpoints.router)

Base.metadata.create_all(bind=engine)


templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")



# pages #
@app.get("/")
async def render_home_page(request: Request):
    # Check query param set after registration redirect and pass flag to template
    registered_flag = request.query_params.get('registered') == 'true'
    return templates.TemplateResponse("home.html", {"request": request, "registered": registered_flag})

@app.get("/about")
async def render_about_page(request: Request):
    return templates.TemplateResponse("about.html", {'request': request})

@app.get("/benefits")
async def render_benefits_page(request: Request):
    return templates.TemplateResponse("benefits.html", {'request': request})

@app.get("/seminars")
async def render_seminars_page(request: Request):
    return templates.TemplateResponse("seminars.html", {'request': request})

@app.get("/contact-us")
async def render_contact_us_page(request: Request):
    return templates.TemplateResponse("contact-us.html", {'request': request})

@app.get("/our-team")
async def render_team_page(request: Request):
    return templates.TemplateResponse("our-team.html", {'request': request})

@app.get("/join-us")
async def render_join_us_page(request: Request):
    return templates.TemplateResponse("register_volunteers.html", {'request': request})

@app.get("/registration-success")
async def render_registration_success_page(request: Request):
    return templates.TemplateResponse("registration_success.html", {'request': request})