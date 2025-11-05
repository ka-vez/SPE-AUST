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
async def register_volunteers(
    request: Request, 
    db: db_dependency, 
    full_name: str = Form(), 
    email: str = Form(), 
    phone_number: str = Form(),
    home_address: str = Form(), 
    state_of_origin: str = Form(),
    is_web: str | None = Form(None)
):
    
    volunteer = Volunteers(
        full_name = full_name,
        email = email,
        phone_number = phone_number,
        home_address = home_address, 
        state_of_origin = state_of_origin,
        registered = False
    )
    db.add(volunteer)
    db.commit()
    
    if is_web == 'true':
        # Use 303 See Other so the browser follows the redirect with GET
        # Redirect to success page instead of home page
        return RedirectResponse(request.url_for('render_registration_success_page'), status_code=status.HTTP_303_SEE_OTHER)
    return {"message": "Volunteer registered successfully"}

@router.get("/executives")
async def get_executives(db: db_dependency):
    all_executives = db.query(Executives).all()
    return all_executives

# @router.post("/register-executives", status_code=status.HTTP_201_CREATED)
# async def register_executives(db: db_dependency, first_name: str = Form(), last_name: str = Form(), phone_number: str = Form() \
#                               ,email: str = Form(), department: str = Form(), file: UploadFile = File(...)):

#     with open("media/"+file.filename, "wb") as image:
#         shutil.copyfileobj(file.file, image)
    
#     url = str("media/"+file.filename)
#     executive = Executives(
#         first_name = first_name,
#         last_name = last_name,
#         phone_number = phone_number,
#         email = email,
#         department = department,
#         image = url
#     )
#     db.add(executive)
#     db.commit()
#     return {"message": "Executive registered successfully"}