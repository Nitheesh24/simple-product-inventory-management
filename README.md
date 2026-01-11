# Simple Product & Inventory Management System

A beginner-friendly backend project built using **Python**, **FastAPI**, and **SQLite**.
This project demonstrates basic backend development skills such as API creation,
database integration, and CRUD operations.

## Features
- Create, read, update, and delete products
- Track product quantity (inventory)
- RESTful API built using FastAPI
- SQLite database for simplicity
- Auto-generated API documentation (Swagger UI)

## Tech Stack
- Python 3
- FastAPI
- SQLAlchemy
- SQLite
- Uvicorn

## Project Structure
simple-product-inventory-management/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── crud.py
│
├── README.md
├── requirements.txt
└── venv/

## How to Run Locally

1. Clone the repository:
   git clone https://github.com/Nitheesh24/simple-product-inventory-management.git

2. Navigate into the project:
   cd simple-product-inventory-management

3. Create and activate virtual environment:
   python -m venv venv
   venv\Scripts\activate

4. Install dependencies:
   pip install -r requirements.txt

5. Run the application:
   uvicorn app.main:app --reload

6. Open browser:
   http://127.0.0.1:8000/docs

## API Endpoints (Examples)
- POST /products/ → Add new product
- GET /products/ → List all products
- GET /products/{id} → Get product by ID
- PUT /products/{id} → Update product
- DELETE /products/{id} → Delete product

## Why This Project?
This project was created to demonstrate:
- Python backend development
- REST API design
- Database interaction using SQL
- Clean and readable project structure

## Author
Nitheesh Thotakura  
GitHub: https://github.com/Nitheesh24
