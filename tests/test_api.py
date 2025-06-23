from fastapi.testclient import TestClient
from app.main import app
from app import crud, models, schemas
from app.database import get_db

client = TestClient(app)

def test_add_product():
    response = client.post("/products/", json={
        "name": "API Product",
        "description": "Test desc",
        "price": 20.5,
        "quantity": 5
    })
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "API Product"

def test_get_products():
    response = client.get("/products/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
