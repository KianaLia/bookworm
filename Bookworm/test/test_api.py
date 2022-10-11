import requests
import json
from jsonschema import validate
from jsonschema import Draft6Validator
import pytest

def test_user_recoms(sample_uid=20163):
    url = 'http://api:5020/user_recoms/{}'.format(sample_uid)
    response = requests.get(url)
    assert response.status_code == 200

def test_model_info(sample_uid=20163, sample_model='actions'):
    url = 'http://api:5020/model_info/{}/{}'.format(sample_model, sample_uid)
    response = requests.get(url)
    assert response.status_code == 200
