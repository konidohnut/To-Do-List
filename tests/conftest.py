from typing import Generator
from fastapi.testclient import TestClient
import pytest

from app.main import app


@pytest.fixture
def test_client() -> Generator[TestClient, None, None]:
    client = TestClient(app)

    yield client
