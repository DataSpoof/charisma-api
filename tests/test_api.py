import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# ✅ Sample valid input (53 features)
valid_payload = {
    "features": [
        120,4,8.5,120.3,45,3.2,500,4.5,120,
        300,2,150,80,10,5,7,20,15,0,
        1,0,0.2,0.3,0.1,2,2048,32,1.5,0,
        0,0,1,0,0,0,0.1,0.2,0.0,0.3,
        0.1,0.2,0.0,60,120,10,5,20,15,100,
        10,2,3
    ]
}

# ❌ Invalid input (wrong length)
invalid_payload = {
    "features": [1, 2, 3]
}


# =========================
# TEST 1: Health Check
# =========================
def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


# =========================
# TEST 2: Valid Prediction
# =========================
def test_prediction_valid():
    response = client.post("/predict", json=valid_payload)
    
    assert response.status_code == 200
    
    data = response.json()
    
    assert "prediction" in data
    assert data["prediction"] in ["malware", "benign"]
    
    assert "confidence" in data
    assert 0 <= data["confidence"] <= 1


# =========================
# TEST 3: Invalid Input
# =========================
def test_prediction_invalid_length():
    response = client.post("/predict", json=invalid_payload)
    
    assert response.status_code in [400, 422]


# =========================
# TEST 4: Missing Key
# =========================
def test_missing_features():
    response = client.post("/predict", json={})
    
    assert response.status_code == 422


# =========================
# TEST 5: Wrong Data Type
# =========================
def test_wrong_type():
    payload = {
        "features": ["a"] * 53
    }
    
    response = client.post("/predict", json=payload)
    
    assert response.status_code == 422