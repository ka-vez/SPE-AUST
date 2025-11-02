from .database import Base
from sqlalchemy import Column, Integer, String, Boolean

class Volunteers(Base):
    __tablename__ = "volunteers"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    phone_number = Column(String)
    email = Column(String)
    department = Column(String)
    other_information = Column(String)
    registered = Column(Boolean)

class Executives(Base):
    __tablename__ = "executives"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    phone_number = Column(String)
    email = Column(String)
    department = Column(String)
    image = Column(String, nullable=True)
