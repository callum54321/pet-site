from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import String, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from dotenv import load_dotenv
import os
from pathlib import Path

# Load env variables
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)
DATABASE_URL = os.getenv("DATABASE_URL")
assert DATABASE_URL is not None, "DATABASE_URL is not set."

# Database initialisation
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


# Pets database table model
class Pet(Base):
    __tablename__ = "pets"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    name: Mapped[str] = mapped_column(String(25), nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    species: Mapped[str] = mapped_column(String(15), nullable=False)
    description: Mapped[str] = mapped_column(String(200))
    url: Mapped[str] = mapped_column(String(500), nullable=False)  # Image URL
    location: Mapped[str] = mapped_column(String(50), nullable=False)


Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
