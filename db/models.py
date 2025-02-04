from .database import Base
from sqlalchemy import Column, Integer, String, Boolean

class Registration(Base):
    __tablename__ = "registration"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    phone_number = Column(String)
    email = Column(String)
    degree_program = Column(String)
    other_information = Column(String)
    registered = Column(Boolean)