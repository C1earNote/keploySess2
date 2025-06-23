# Custom FastAPI CRUD Server

## 📌 Features
- Create, Read, Update, Delete products
- SQLite + SQLAlchemy ORM
- Fully RESTful API with FastAPI

## 🔧 How to Run

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```
if uvicorn dosen't work try:
```bash
pip install -r requirements.txt
python -m uvicorn main:app
```

## 📦 API Endpoints

### POST/products/
Create a new Product
### GET/products/
Get all products
### GET/products/{id}
Get a product by ID
### PUT/products/{id}
Update product info by ID
### DELETE/products/{id}
Delete a product