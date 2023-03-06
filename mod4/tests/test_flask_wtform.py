import unittest
from flask_wtform import app

class TestFlaskWtform(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()
        self.base_url = 'https://localhost/registration'

    def test_without_fall(self):
        response = self.app.post(self.base_url, data={"email": "test@example.com", "phone": 7777777777, "name": "Bogdan", "address": "Lenina", "index": 5})
        assert (response.status_code == 200)

    def test_with_wrong_email(self):
        response = self.app.post(self.base_url, data={"email": "testexample.com", "phone": 7777777777, "name": "Bogdan", "address": "Lenina", "index": 5})
        assert (response.status_code == 400)

    def test_with_wrong_number_email(self):
        response = self.app.post(self.base_url, data={"email": 77, "phone": 7777777777, "name": "Bogdan", "address": "Lenina", "index": 5})
        assert (response.status_code == 400)

    def test_with_wrong_bigger_phone(self):
        response = self.app.post(self.base_url, data={"email": "test@example.com", "phone": 77777778777, "name": "Bogdan", "address": "Lenina", "index": 5})
        assert (response.status_code == 400)

    def test_with_wrong_string_phone(self):
        response = self.app.post(self.base_url, data={"email": "test@example.com", "phone": 'number', "name": "Bogdan", "address": "Lenina", "index": 5})
        assert (response.status_code == 400)

    def test_with_wrong_string_index(self):
        response = self.app.post(self.base_url, data={"email": "test@example.com", "phone": 7777777777, "name": "Bogdan", "address": '12', "index": 'yes'})
        assert (response.status_code == 400)

    def test_without_email(self):
        response = self.app.post(self.base_url, data={"phone": 7777777777, "name": "Bogdan", "address": "Lenina", "index": 5})
        assert (response.status_code == 400)

    def test_without_phone(self):
        response = self.app.post(self.base_url, data={"email": "test@example.com", "name": "Bogdan", "address": "Lenina", "index": 5})
        assert (response.status_code == 400)

    def test_without_name(self):
        response = self.app.post(self.base_url, data={"email": "test@example.com", "phone": 7777777777, "address": "Lenina", "index": 5})
        assert (response.status_code == 400)

    def test_without_address(self):
        response = self.app.post(self.base_url, data={"email": "test@example.com", "phone": 7777777777, "name": "Bogdan", "index": 5})
        assert (response.status_code == 400)

    def test_without_index(self):
        response = self.app.post(self.base_url, data={"email": "test@example.com", "phone": 7777777777, "name": "Bogdan", "address": "Lenina"})
        assert (response.status_code == 400)