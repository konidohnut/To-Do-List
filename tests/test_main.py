from fastapi.testclient import TestClient
from fastapi import status


def test_health_check(test_client: TestClient) -> None:
    response = test_client.get("/")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["detail"] == "ok"
    assert data["result"] == "working"
