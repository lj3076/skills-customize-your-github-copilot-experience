from fastapi.testclient import TestClient

from starter_code import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Item API"}


# Add tests for listing items, retrieving an item, and requesting a missing item.