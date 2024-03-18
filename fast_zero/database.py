from sqlalchemy import create_engine  # pyright: ignore
from sqlalchemy.orm import Session  # pyright: ignore

from fast_zero.settings import Settings

engine = create_engine(Settings().DATABASE_URL)  # pyright: ignore

def get_session():
    with Session(engine) as session:
        yield session
