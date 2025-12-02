#for  database connection
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./notes.db"

#creating DB engine
engine  = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} #only for sqlite
)

#creating a configured "Session" class

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

#Base class for our models
Base = declarative_base()

# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()