from django.test import TestCase
from rest_framework.test import RequestsClient, APIRequestFactory
from rest_framework.utils import json


# Create your tests here.

class TestApi(TestCase):
    def test_api_swagger(self):
        client = RequestsClient()
        response = client.get('http://127.0.0.1:8000/api/swagger/')
        assert response.status_code == 200

    def test_list(self):
        client = RequestsClient()
        response = client.get('http://127.0.0.1:8000/api/list/')
        assert response.status_code == 200



