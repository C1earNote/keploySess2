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
<<<<<<< HEAD
pip install -r requirements.txt
python -m uvicorn main:app
=======
python -m uvicorn app.main:app --reload
```
Visit: `http://127.0.0.1:8000/docs`

### Open the Frontend
Just open `index.html` in your browser (double click or open with live server)

---

## ✅ API Endpoints

| Method | Endpoint          | Description              |
|--------|-------------------|--------------------------|
| POST   | `/products/`      | Add a new product        |
| GET    | `/products/`      | Get all products         |
| GET    | `/products/{id}`  | Get product by ID        |
| PUT    | `/products/{id}`  | Update product by ID     |
| DELETE | `/products/{id}`  | Delete product by ID     |

---

## 🧪 How to Run Tests

### Install Pytest Tools
```bash
pip install pytest pytest-cov httpx
>>>>>>> e102f4004565baaa7a675e793079f5761ba4d154
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