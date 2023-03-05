import unittest
from freezegun import freeze_time
from hello_world import app

class TestMaxNumber(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/hello-world/'

    def test_can_get_correct_username_with_weekdate(self):
        username = 'username'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(username in response_text)

    @freeze_time("2023-03-04")
    def test_can_get_correct_weekday(self):
        weekday = "Хорошей субботы"
        response = self.app.get(self.base_url + 'username')
        response_text = response.data.decode()
        self.assertTrue(weekday in response_text.split('.')[1])