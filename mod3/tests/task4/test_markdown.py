import unittest
from task4 import markdown


class TestSalary(unittest.TestCase):
    def setUp(self):
        self.person = markdown.Person('Bogdan', 2003, 'St. Lenina')

    def test_get_age(self):
        self.assertEqual(20, self.person.get_age())

    def test_get_name(self):
        self.assertEqual('Bogdan', self.person.get_name())

    def test_set_name(self):
        self.person.set_name("Alex")
        self.assertEqual('Alex', 'Alex')

    def test_set_address(self):
        self.person.set_address("St. Mira")
        self.assertEqual('St. Mira', 'St. Mira')

    def test_get_address(self):
        self.assertEqual('St. Lenina', self.person.get_address())

    def test_is_homeless(self):
        self.person.set_address("St. Voroshilova")
        self.assertEqual(False, self.person.is_homeless())

