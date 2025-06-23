from app.database import SessionLocal
from app.models import Product
from app.main import app
from fastapi.testclient import TestClient
from app import crud, models, schemas
from app.database import get_db


client = TestClient(app)

def test_crud_flow():
    # Create
    response = client.post("/products/", json={
        "name": "IntegrationTest",
        "description": "End-to-end",
        "price": 99.0,
        "quantity": 9
    })
    assert response.status_code == 200
    product_id = response.json()["id"]

    # Read
    get_res = client.get(f"/products/{product_id}")
    assert get_res.status_code == 200
    assert get_res.json()["id"] == product_id

    # Delete
    del_res = client.delete(f"/products/{product_id}")
    assert del_res.status_code == 200
