"""Test suite."""
from fastapi.testclient import TestClient

from mainapp.main import app

# Create a Test Client for FastAPI app
client = TestClient(app)
# Test FastAPI using TestClient
def test_root() -> None:
    """Test main page."""
    response = client.get("/")
    assert response.status_code == 200  # noqa: S101, PLR2004
    assert response.json() == {"message": "Hello World"} # noqa: S101
