# FastAPI 7-Day Learning Roadmap
This roadmap is designed to get you building robust, modern APIs quickly. Each day builds on the last, ensuring a solid foundation.

## 🚀 Day 1: Foundations & First App
Start by setting up your environment and understanding the core mechanics of a web API.

- Python Essentials:
  - Async/Await: FastAPI is built on asyncio. Understand how async functions and await calls work.
```python
  # Example: Simple async function
import asyncio

async def fetch_data():
    await asyncio.sleep(1) # Simulate network delay
    return {"data": "Hello from async!"}

async def main():
    result = await fetch_data()
    print(result)

# asyncio.run(main()) # Run this outside FastAPI for standalone testing
```

  - Type Hinting: Crucial for FastAPI's automatic validation and documentation.
```python
# Example: Type hints
def greet(name: str, age: int) -> str:
    return f"Hello, {name}! You are {age} years old."
```

- HTTP & REST Basics: Review HTTP methods (GET, POST, PUT, DELETE), status codes (200 OK, 404 Not Found), and the concept of RESTful APIs.
- Setup:
  - Install Python 3.8+
  - Create a virtual environment: python -m venv .venv
  - Activate it: source .venv/bin/activate (Linux/macOS) or .venv\Scripts\activate (Windows)
  - Install FastAPI and Uvicorn: pip install "fastapi[all]" uvicorn
- Hands-on Example: Your First FastAPI App

```python
# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"}

# Run in your terminal: uvicorn main:app --reload
# Then open http://127.0.0.1:8000/ in your browser.
```

##  🛣️ Day 2: Routes, Path & Query Parameters
Learn how to define different API endpoints and extract information from the URL.

- Basic Routes: How to define endpoints for different URLs.
- Path Parameters: Extract values directly from the URL path. FastAPI automatically validates and converts types.

```python
# Example: Path parameters
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int): # item_id will be an integer
    return {"item_id": item_id}
```

- Query Parameters: Extract values from the query string (after ?). They are optional by default.
```python
# Example: Query parameters
from fastapi import FastAPI

app = FastAPI()

@app.get("/search/")
async def search_items(query: str, skip: int = 0, limit: int = 10):
    # query is required, skip defaults to 0, limit defaults to 10
    return {"query": query, "skip": skip, "limit": limit}
```

- Hands-on:
  - Create an endpoint GET /users/{user_id} that returns user details.
  - Create an endpoint GET /products/ that accepts optional category and max_price query parameters.
  - Explore the automatic API docs at http://127.0.0.1:8000/docs (Swagger UI) and http://127.0.0.1:8000/redoc (ReDoc).

## 📦 Day 3: Request Body & Pydantic Validation  
Understand how to receive data in the request body (e.g., for POST or PUT requests) and use Pydantic for robust data validation.

- Request Body: How to define data models for incoming requests.
- Pydantic BaseModel: FastAPI uses Pydantic for data validation, serialization, and deserialization. This is a core strength!

```python
# Example: Request Body with Pydantic
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.post("/items/")
async def create_item(item: Item): # item is a Pydantic model
    return {"message": "Item created successfully!", "item": item}
```

- Hands-on:
  - Create a POST /products/ endpoint that accepts a JSON request body conforming to a Product Pydantic model (e.g., name: str, price: float, is_available: bool).
  - Test sending valid and invalid JSON to observe Pydantic's automatic validation errors.

## 🔗 Day 4: Dependencies & Error Handling   

Learn to reuse logic across your API and how to respond gracefully when things go wrong.

- Dependency Injection: A powerful feature to share code, manage database sessions, or handle authentication.

```python
# Example: Dependency
from fastapi import FastAPI, Depends, HTTPException, status

app = FastAPI()

# A simple dependency to check for an API key
async def get_api_key(api_key: str):
    if api_key != "SECRET_KEY":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key"
        )
    return api_key

@app.get("/protected-data/")
async def read_protected_data(api_key: str = Depends(get_api_key)):
    return {"data": "This is sensitive information."}
```

- Error Handling: Raise HTTPException for standard HTTP error responses.

```python
# Example: Error Handling
from fastapi import FastAPI, HTTPException, status

app = FastAPI()

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    if user_id != 1:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return {"user_id": user_id, "name": "Test User"}
```

- Hands-on:
  - Create a dependency to simulate user authentication (e.g., by checking a header).
  - Apply this dependency to a few of your routes.
  - Implement custom error handling for a specific scenario (e.g., if a resource cannot be updated, return a 409 Conflict).

## 🔒 Day 5: Security & 💾 Databases (Basic)  

Implement basic authentication and connect your API to a database.

- Authentication & Security:
  - OAuth2 with Bearer Tokens: A common pattern for API authentication.
  - Using Security from fastapi.security.
  - Password Hashing: Use passlib (e.g., bcrypt) for securely storing passwords.
- Database Integration (SQLite + SQLAlchemy):
  - SQLAlchemy ORM: A powerful ORM (Object Relational Mapper) for Python.
  - Define models representing your database tables.
  - Create and manage database sessions using dependencies.

```python
# Example: Basic SQLAlchemy setup (conceptual, requires more files)
# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db" # Or "postgresql://user:password@host/db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# models.py
from sqlalchemy import Column, Integer, String
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

# main.py (using the session)
from fastapi import Depends
from sqlalchemy.orm import Session
# ... other imports ...
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/")
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # ... logic to add user to db ...
    pass
```

- Hands-on:
  - Implement a /token endpoint for users to get an access token.
  - Protect an endpoint (e.g., GET /current_user/) that requires a valid bearer token.
  - Set up a simple SQLite database and use SQLAlchemy to save and retrieve data (e.g., create an endpoint to create a User and another to read all users).

## 🧪 Day 6: Testing & Deployment  

Ensure your API works correctly and prepare it for real-world usage.

- Testing FastAPI: Use FastAPI's TestClient for fast, efficient testing.

```python
# Example: Testing
from fastapi.testclient import TestClient
from main import app # Assuming your FastAPI app is in main.py

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPI!"}

def test_read_item():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"item_id": 1}

# Run with: pytest your_test_file.py

```

- CORS (Cross-Origin Resource Sharing): Allow your frontend applications to interact with your API from different domains.

```python
# Example: CORS
from fastapi.middleware.cors import CORSMiddleware
# ... your app definition ...

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # For development, use specific origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

- Deployment Concepts: Understand how to deploy FastAPI apps (e.g., Docker, Heroku, AWS ECS/Lambda). Focus on running Uvicorn with a production-ready setup (e.g., Gunicorn + Uvicorn workers).
- Hands-on:
  - Write basic tests for your POST and GET endpoints, verifying status codes and response bodies.
  - Add CORS middleware to your application.
  - (Optional but recommended) Create a Dockerfile for your application.

## ⚙️ Day 7: Advanced Features & Project Time!  

Explore powerful advanced concepts and build a small project to solidify your knowledge.

- Middleware: Create custom middleware for tasks like logging, request ID injection, or timing.

```python
# Example: Custom Middleware
from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response
import time

class TimingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        response.headers["X-Process-Time"] = str(process_time)
        print(f"Request took {process_time:.4f} seconds")
        return response

app.add_middleware(TimingMiddleware)
```

- Background Tasks: Run long-running tasks without blocking the HTTP response.

```python
# Example: Background Task
from fastapi import FastAPI, BackgroundTasks

app = FastAPI()

def write_notification(email: str, message: str = ""):
    with open("log.txt", mode="a") as email_file:
        content = f"notification for {email}: {message}\n"
        email_file.write(content)

@app.post("/send-notification/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_notification, email, message="Welcome to our service!")
    return {"message": "Notification sent in background"}
```

- WebSockets (Optional): Dive into real-time communication if you're feeling adventurous.
- Hands-on Project:
  - Choose a small project: A simple blog API (users, posts, comments), a task manager, or a simple e-commerce product catalog.
  - Implement CRUD: Build endpoints for creating, reading, updating, and deleting resources.
  - Apply learned concepts: Use Pydantic models for request/response, dependencies for database sessions or authentication, error handling, and maybe a background task.
  - This is your chance to tie everything together!