import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()

SEVALA_DB_URL = os.getenv("SEVALA_DB_URL")

if not SEVALA_DB_URL:
    raise ValueError("SEVALA_DB_URL environment variable is not set. Please check your .env file.")

# Fix postgres:// to postgresql:// for SQLAlchemy compatibility
if SEVALA_DB_URL.startswith("postgres://"):
    SEVALA_DB_URL = SEVALA_DB_URL.replace("postgres://", "postgresql://", 1)

print(f"Connecting to database: {SEVALA_DB_URL.split('@')[0]}@***")

# SQL_DATABASE_URL = "sqlite:///registration.db"
# engine = create_engine(SQL_DATABASE_URL, connect_args={'check_same_thread': False})
engine = create_engine(SEVALA_DB_URL)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()