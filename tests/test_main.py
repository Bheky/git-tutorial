from fastapi.testclient import TestClient
from src.main import app

# Setup the test client
client = TestClient(app)


# Basic unit test for the endpoint
def test_hello():
    response = client.get("/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data == "Hello, World!"

