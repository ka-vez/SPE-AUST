from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQL_DATABASE_URL = "sqlite:///registration.db"

engine = create_engine(SQL_DATABASE_URL, connect_args={'check_same_thread': False})

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()