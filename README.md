# 🛠️ Product Manager API

A CRUD-based API server built using **FastAPI** and **SQLite**, featuring:
- Backend APIs for managing products
- Frontend in HTML + JavaScript
- Unit, integration, and API tests
- ~85% test coverage using `pytest`

---

## 📦 Features
- Add, update, delete, and fetch products
- Database-backed using SQLAlchemy ORM
- Swagger UI interface at `/docs`
- Secure CORS handling for frontend

---

## 🔧 Tech Stack
- FastAPI
- SQLite
- SQLAlchemy
- Pydantic
- HTML + JS (Vanilla)
- Pytest + HTTPX + pytest-cov (for testing)

---

## ▶️ How to Run Locally

### Install Requirements
```bash
pip install -r requirements.txt
```

### Start the Backend Server
```bash
uvicorn app.main:app --reload
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
```

### Run All Tests with Coverage
```bash
$env:PYTHONPATH="."
python -m pytest --cov=app tests/
```

### Generate Coverage Report (HTML)
```bash
pytest --cov=app --cov-report=html tests/
```
Opens in: `htmlcov/index.html`

---

## 🧪 Test File Overview
- `tests/test_crud.py`: Unit tests for logic layer (create, fetch, delete)
- `tests/test_api.py`: Endpoint tests via FastAPI TestClient
- `tests/test_integration.py`: End-to-end CRUD workflow validation
- `tests/conftest.py`: Configures import paths for tests

---

## 🧾 Manual Test Cases

### ✅ POST /products/
- **Valid Product** → `200 OK`
- **Missing fields** → `422 Unprocessable Entity`

### ✅ GET /products/
- **Returns list of all products** → `200 OK`

### ✅ GET /products/{id}
- **Existing ID** → `200 OK`
- **Invalid ID** → `404 Not Found`

### ✅ DELETE /products/{id}
- **Valid ID** → `200 OK`
- **Invalid ID** → `404 Not Found`

---

## 🧠 Learnings
- Built backend APIs from scratch with FastAPI
- Understood database integration via SQLAlchemy
- Implemented full test suite: unit + integration + API
- Fixed CORS and async data loading on frontend

---

## 📤 Author
Built during the Keploy Fellowship testing task by Tanishq Nigam
