from db.database import SessionLocal, engine
from db.models import Base, Volunteers, Executives

import shutil
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status, UploadFile, File, Form, Request
from fastapi.responses import RedirectResponse
from schemas import RegisterVolunteerRequest, RegisterExecutiveRequest


router = APIRouter(prefix="/api", tags=['api'])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

# endpoints #
@router.get("/volunteers")
async def get_volunteers(db: db_dependency):
    all_volunteers = db.query(Volunteers).all()
    return all_volunteers

@router.post("/register-volunteers", status_code=status.HTTP_201_CREATED)
async def register_volunteers(request: Request, db: db_dependency, first_name: str = Form(), last_name:str = Form(), phone_number: str = Form() \
                              ,email: str = Form(), department: str = Form(), other_information: str = Form(), registered: bool = False, is_web: str | None = Form()):
    volunteer = Volunteers(
        first_name = first_name,
        last_name = last_name,
        phone_number = phone_number,
        email = email,
        department = department,
        other_information = other_information,
        registered = registered
    )
    db.add(volunteer)
    db.commit()
    print(is_web)
    if is_web == 'true':
        return RedirectResponse(request.url_for('render_home_page'))
    return {"message": "Volunteer registered successfully"}

@router.get("/executives")
async def get_executives(db: db_dependency):
    all_executives = db.query(Executives).all()
    return all_executives

@router.post("/register-executives", status_code=status.HTTP_201_CREATED)
async def register_volunteers(db: db_dependency, first_name: str = Form(), last_name:str = Form(), phone_number: str = Form() \
                              ,email: str = Form(), department: str = Form(), file: UploadFile = File):

    with open("media/"+file.filename, "wb") as image:
        shutil.copyfileobj(file.file, image)
    
    url = str("media/"+file.filename)
    executive = Executives(
        first_name = first_name,
        last_name = last_name,
        phone_number = phone_number,
        email = email,
        department = department,
        image = url
    )
    db.add(executive)
    db.commit()
    return {"message": "Executive registered successfully"}