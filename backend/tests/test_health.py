from fastapi.testclient import TestClient
from app.main import app
from app.db.session import get_db
from app.models import User
from app.core.security import hash_password

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
    db = next(get_db())
    email = "ci-crop@example.com"
    user = db.query(User).filter(User.email == email).first()
    if not user:
        user = User(
            full_name="CI Crop User",
            email=email,
            password_hash=hash_password("TestPassword123!"),
        )
        db.add(user)
        db.commit()
        db.refresh(user)

    login_response = client.post(
        "/api/v1/auth/login",
        json={"email": email, "password": "TestPassword123!"},
    )
    assert login_response.status_code == 200

    token = login_response.json()["access_token"]
    response = client.post(
        "/api/v1/crop-recommendation",
        json={
            "nitrogen": 90,
            "phosphorus": 42,
            "potassium": 43,
            "temperature": 25,
            "humidity": 80,
            "ph": 6.5,
            "rainfall": 200,
        },
        headers={"Authorization": "Bearer " + token},
    )
    assert response.status_code in (200, 503)
