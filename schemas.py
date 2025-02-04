from pydantic import BaseModel, Field

class RegistrationRequest(BaseModel):
    first_name: str
    last_name :str
    phone_number: str
    email: str
    degree_program: str
    other_information: str
    registered: bool = Field(default=False)