from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_api_status():
    response = client.get("/api/v1/status")
    assert response.status_code == 200
    assert response.json()["api"] == "v1"

def test_crop_model_pending():
    response = client.post("/api/v1/crop-recommendation", json={
        "nitrogen": 90, "phosphorus": 42, "potassium": 43,
        "temperature": 25, "humidity": 80, "ph": 6.5, "rainfall": 200
    })
    assert response.status_code in (200, 503)
