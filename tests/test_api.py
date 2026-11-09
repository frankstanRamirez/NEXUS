from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["name"] == "NEXUS"
    assert response.json()["message"] == "NEXUS is online"


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "online"
    assert response.json()["service"] == "NEXUS API"
    assert "timestamp" in response.json()
