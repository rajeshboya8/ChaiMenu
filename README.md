# ☕ Chai Point – Menu API

A simple REST API built using **FastAPI** and **Pydantic** to manage and retrieve Chai Point menu items.

This project is created as a beginner-friendly hands-on application to understand FastAPI fundamentals, REST APIs, request handling, response models, query parameters, and HTTP exceptions.

## 🚀 Features

- Get a welcome message.
- Retrieve all menu items.
- Filter menu items by category.
- Retrieve a specific menu item using its ID.
- Validate API responses using Pydantic models.
- Handle errors using HTTPException.
- Interactive API documentation using Swagger UI and ReDoc.

## 🛠️ Tech Stack

- Python
- FastAPI
- Pydantic
- Uvicorn

## 📁 Project Structure

```text
ChaiMenu/
│
├── main.py          # FastAPI application and endpoints
├── models.py        # Pydantic data models
├── data.py          # Static menu data
├── README.md        # Project documentation
└── .gitignore       # Git ignored files
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/rajeshboya8/ChaiMenu.git
cd ChaiMenu
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows:**

```powershell
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install fastapi uvicorn
```

### 5. Run the application

```bash
uvicorn main:app --reload
```

The application will run at:

`http://127.0.0.1:8000`

## 📌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Welcome message |
| GET | `/menu` | Retrieve all menu items |
| GET | `/menu?category=Chai` | Filter items by category |
| GET | `/menu/{item_id}` | Retrieve a menu item by ID |

## 📖 API Documentation

FastAPI automatically generates interactive API documentation.

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

## 🎯 Learning Objectives

Through this project, I am learning:

- FastAPI application setup.
- HTTP methods and REST API fundamentals.
- Path parameters and query parameters.
- Pydantic BaseModel and response validation.
- HTTPException and status codes.
- API documentation with Swagger UI and ReDoc.
- Running applications using Uvicorn.


**Rajesh**

GitHub: https://github.com/rajeshboya8
