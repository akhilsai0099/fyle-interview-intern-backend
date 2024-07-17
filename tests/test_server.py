# tests/test_server.py

from marshmallow.exceptions import ValidationError
import pytest
from flask import jsonify, json
from core.server import app
from core.libs.exceptions import FyleError
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import HTTPException

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_ready(client):
    response = client.get('/')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 'ready'
    assert 'time' in data
