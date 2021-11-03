import requests
import pytest

# may need to modify clf reference and model path in apps.py as well
# may need to modify this path
from dockerfile.apps.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_client(client):
    r = client.get('/')
    print("\n====== Result TEST_CLIENT ======")
    print(r.data)
    print("TEST PASSED!")

def test_predict1(client):
    r = client.get('/predict?age=15&health=5&absences=5&studytime=4&goout=5&failures=2&famrel=5')
    print("\n====== Result TEST_PREDICT ======")
    print(int(r.data))
    assert(int(r.data) == 0)
    print("TEST PASSED!")

def test_predict2(client):
    r = client.get('/predict?age=15&health=5&absences=0&studytime=4&goout=0&failures=0&famrel=5')
    print("\n====== Result TEST_PREDICT ======")
    print(int(r.data))
    assert(int(r.data) == 0)
    print("TEST PASSED!")