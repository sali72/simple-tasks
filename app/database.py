from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.config import POSTGRES_URL, APP_DEBUG

engine = create_engine(POSTGRES_URL, echo=APP_DEBUG)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

db_session = SessionLocal()
Base = declarative_base()
