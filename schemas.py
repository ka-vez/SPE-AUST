from pydantic import BaseModel, Field

class RegisterVolunteerRequest(BaseModel):
    first_name: str
    last_name :str
    phone_number: str
    email: str
    department: str
    other_information: str
    registered: bool = Field(default=False)

class RegisterExecutiveRequest(BaseModel):
    first_name: str
    last_name :str
    phone_number: str
    email: str
    department: str