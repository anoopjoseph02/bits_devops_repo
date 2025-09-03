import pytest
from aceest_fitness.app import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_health(client):
    res = client.get('/health')
    assert res.status_code == 200
    assert res.get_json()['status'] == 'ok'

def test_add_and_list_workout(client):
    res = client.post('/workouts', json={'workout': 'Push Ups', 'duration': 15})
    assert res.status_code == 201
    data = res.get_json()
    assert data['workout'] == 'Push Ups'
    res = client.get('/workouts')
    assert res.status_code == 200
    assert any(w['workout'] == 'Push Ups' for w in res.get_json())

def test_bmi(client):
    res = client.post('/bmi', json={'height_cm': 180, 'weight_kg': 75})
    assert res.status_code == 200
    data = res.get_json()
    assert 'bmi' in data
    assert 'category' in data
