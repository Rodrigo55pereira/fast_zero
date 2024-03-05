import pytest  # pyright: ignore
from fastapi.testclient import TestClient
from sqlalchemy import create_engine  # pyright: ignore
from sqlalchemy.orm import sessionmaker  # pyright: ignore

from fast_zero.app import app
from fast_zero.models import Base  # pyright: ignore


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def session():
    engine = create_engine('sqlite:///:memory:')
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    yield Session()
    Base.metadata.drop_all(engine)
