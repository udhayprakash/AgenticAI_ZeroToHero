"""
Testing FastAPI Endpoints

Demonstrates testing FastAPI applications and async code.

Run tests with:
    uv add --dev pytest
    uv add --dev pytest-asyncio
    uv run pytest test_fastapi.py -v
"""

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from pydantic import BaseModel


# ============================================================================
# EXAMPLE: Simple FastAPI App
# ============================================================================

class Item(BaseModel):
    name: str
    price: float
    tax: float = 0.1


app = FastAPI()

# In-memory database
items_db = {}
next_id = 1


@app.get("/")
async def root():
    return {"message": "Hello"}


@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    if item_id not in items_db:
        return {"detail": "Item not found"}
    return items_db[item_id]


@app.post("/items", response_model=Item, status_code=201)
async def create_item(item: Item):
    global next_id
    items_db[next_id] = item.dict()
    next_id += 1
    return item.dict()


@app.get("/items")
async def list_items():
    return list(items_db.values())


@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    if item_id not in items_db:
        return {"detail": "Item not found"}
    del items_db[item_id]
    return {"message": "Deleted"}


# ============================================================================
# TESTS
# ============================================================================

@pytest.fixture
def client():
    """Provide FastAPI test client"""
    return TestClient(app)


@pytest.fixture(autouse=True)
def clear_db():
    """Clear database before each test"""
    global next_id
    items_db.clear()
    next_id = 1
    yield


# ============================================================================
# 1. BASIC HTTP TESTS
# ============================================================================

def test_root(client):
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello"}


def test_get_nonexistent_item(client):
    """Test getting non-existent item"""
    response = client.get("/items/999")
    assert response.status_code == 200
    assert "detail" in response.json()


# ============================================================================
# 2. POST REQUESTS
# ============================================================================

def test_create_item(client):
    """Test creating an item"""
    item = {"name": "Widget", "price": 9.99, "tax": 0.1}
    response = client.post("/items", json=item)
    
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Widget"
    assert data["price"] == 9.99


def test_create_item_without_optional_fields(client):
    """Test creating item without optional tax field"""
    item = {"name": "Widget", "price": 9.99}
    response = client.post("/items", json=item)
    
    assert response.status_code == 201
    data = response.json()
    assert data["tax"] == 0.1  # Default value


def test_create_item_validation_error(client):
    """Test validation error on missing required fields"""
    item = {"name": "Widget"}  # Missing price
    response = client.post("/items", json=item)
    
    # FastAPI returns 422 for validation errors
    assert response.status_code == 422
    assert "detail" in response.json()


# ============================================================================
# 3. GET REQUESTS WITH PARAMS
# ============================================================================

def test_list_empty_items(client):
    """Test listing items when database is empty"""
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json() == []


def test_list_items(client):
    """Test listing multiple items"""
    # Create items
    client.post("/items", json={"name": "Item1", "price": 5.0})
    client.post("/items", json={"name": "Item2", "price": 10.0})
    
    response = client.get("/items")
    assert response.status_code == 200
    items = response.json()
    assert len(items) == 2


# ============================================================================
# 4. DELETE REQUESTS
# ============================================================================

def test_delete_item(client):
    """Test deleting an item"""
    # Create item
    create_response = client.post("/items", json={"name": "Widget", "price": 9.99})
    # Delete item (ID is 1 because next_id starts at 1 and gets incremented)
    delete_response = client.delete("/items/1")
    
    assert delete_response.status_code == 200
    assert delete_response.json() == {"message": "Deleted"}


def test_delete_nonexistent_item(client):
    """Test deleting non-existent item"""
    response = client.delete("/items/999")
    assert response.status_code == 200
    assert "detail" in response.json()


# ============================================================================
# 5. WORKFLOW TESTS
# ============================================================================

def test_create_retrieve_delete_workflow(client):
    """Test complete CRUD workflow"""
    # Create
    create_response = client.post(
        "/items",
        json={"name": "Test Item", "price": 99.99}
    )
    assert create_response.status_code == 201
    item_id = 1  # First item
    
    # Retrieve
    get_response = client.get(f"/items/{item_id}")
    assert get_response.status_code == 200
    assert get_response.json()["name"] == "Test Item"
    
    # Delete
    delete_response = client.delete(f"/items/{item_id}")
    assert delete_response.status_code == 200
    
    # Verify deleted
    get_response = client.get(f"/items/{item_id}")
    assert "detail" in get_response.json()


# ============================================================================
# 6. TESTING WITH QUERY PARAMETERS
# ============================================================================

@app.get("/search")
async def search_items(query: str = "", min_price: float = 0.0):
    """Search items by name and price"""
    results = []
    for item in items_db.values():
        if (query.lower() in item.get("name", "").lower() and
            item.get("price", 0) >= min_price):
            results.append(item)
    return results


def test_search_items(client):
    """Test search with query parameters"""
    # Create items
    client.post("/items", json={"name": "Expensive Widget", "price": 100.0})
    client.post("/items", json={"name": "Cheap Widget", "price": 5.0})
    client.post("/items", json={"name": "Gadget", "price": 50.0})
    
    # Search
    response = client.get("/search?query=widget&min_price=10")
    assert response.status_code == 200
    results = response.json()
    assert len(results) == 1
    assert results[0]["name"] == "Expensive Widget"


# ============================================================================
# 7. RESPONSE CODES
# ============================================================================

def test_response_status_codes(client):
    """Test various response status codes"""
    # 200 OK
    response = client.get("/")
    assert response.status_code == 200
    
    # 201 Created
    response = client.post("/items", json={"name": "Item", "price": 10})
    assert response.status_code == 201
    
    # 422 Unprocessable Entity (validation error)
    response = client.post("/items", json={"name": "Item"})  # Missing price
    assert response.status_code == 422


# ============================================================================
# 8. HEADERS AND COOKIES
# ============================================================================

@app.get("/protected")
async def protected_endpoint(authorization: str = None):
    """Endpoint that checks authorization header"""
    if not authorization:
        return {"error": "Missing auth"}
    return {"message": "Authorized"}


def test_with_headers(client):
    """Test with custom headers"""
    response = client.get(
        "/protected",
        headers={"Authorization": "Bearer token123"}
    )
    assert response.status_code == 200
    assert response.json()["message"] == "Authorized"


def test_missing_header(client):
    """Test missing required header"""
    response = client.get("/protected")
    assert response.status_code == 200
    assert "error" in response.json()
