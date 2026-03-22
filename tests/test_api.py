from fastapi.testclient import TestClient
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app_api.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200