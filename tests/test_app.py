from fastapi.testclient import TestClient
from Cotacao import app

def test_app_response_200():
    with TestClient(app) as client:
        response = client.get('/cotacao')
        assert response.status_code == 200

def test_app_response_404():
    with TestClient(app) as client:
        response = client.get('/dolar')
        assert response.status_code == 404

def test_app_home():
    with TestClient(app) as client:
        response = client.get('/')
        assert response.status_code == 404

def test_app_swagger():
    with TestClient(app) as client:
        response = client.get('/docs')
        assert response.status_code == 200
