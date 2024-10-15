import pytest
from main import app  # Ensure you import your Flask app correctly

@pytest.fixture
def client():
    """Fixture for testing Flask app."""
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test the home page."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'{"message":"Welcome to the AI-Powered Conflict Resolution Mediator!"}' in response.data

def test_resolve_conflict(client):
    """Test the conflict resolution endpoint."""
    response = client.post('/api/resolve', json={
        "party1": "I feel unheard in this situation.",
        "party2": "I think you are not considering my perspective."
    })
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['success'] is True  # Ensure the success key is present
    assert 'resolved_conflict' in json_data  # Check if resolved_conflict key exists

def test_invalid_resolve_request(client):
    """Test the conflict resolution endpoint with invalid data."""
    response = client.post('/api/resolve', json={})
    assert response.status_code == 400  # Expecting bad request for empty input
    assert b'Missing data' in response.data  # Check for specific error message
