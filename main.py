from db.database import SessionLocal, engine
from db.models import Base, Registration
from schemas import RegistrationRequest

from typing import Annotated
from fastapi import FastAPI, Depends, status, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session


app = FastAPI()

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

db_dependency = Annotated[Session, Depends(get_db)]

# pages #
@app.get("/")
async def render_home_page(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

# endpoints #
@app.get("/users")
async def get_registered_users(db: db_dependency):
    all_registered_users = db.query(Registration).all()
    return all_registered_users

@app.post("/register", status_code=status.HTTP_201_CREATED)
async def register_users(db: db_dependency, registration_request: RegistrationRequest):
    user = Registration(**registration_request.model_dump())
    db.add(user)
    db.commit()
    print(user)
    return {"message": "Registered Successfully"}