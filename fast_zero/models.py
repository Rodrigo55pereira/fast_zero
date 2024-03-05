from sqlalchemy.orm import DeclarativeBase  # pyright: ignore
from sqlalchemy.orm import Mapped  # pyright: ignore
from sqlalchemy.orm import mapped_column  # pyright: ignore


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    password: Mapped[str]
    email: Mapped[str]
