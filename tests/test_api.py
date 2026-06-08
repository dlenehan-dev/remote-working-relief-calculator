from fastapi.testclient import TestClient

from api import app

client = TestClient(app)


def test_home_endpoint():
    response = client.get("/")

    assert response.status_code == 200

    assert response.json() == {
        "message": "Remote Relief API is running."
    }


def test_relief_calculation():
    payload = {
        "electricity": 1000,
        "gas": 800,
        "broadband": 400,
        "year": 2024,
        "remote_days": 180,
        "employer_contribution": 0,
    }

    response = client.post(
        "/relief",
        json=payload,
    )

    assert response.status_code == 200

    data = response.json()

    assert data["year"] == 2024
    assert data["remote_days"] == 180

    assert data["relief"] > 0


def test_negative_electricity_rejected():
    payload = {
        "electricity": -100,
        "gas": 800,
        "broadband": 400,
        "year": 2024,
        "remote_days": 180,
        "employer_contribution": 0,
    }

    response = client.post(
        "/relief",
        json=payload,
    )

    assert response.status_code == 422