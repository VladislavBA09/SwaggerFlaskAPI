import requests
import os

BASE_URL = f"http://localhost:{os.getenv('PORT', 5000)}"

def test_health_check():
    response = requests.get(f"{BASE_URL}/api/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
