import unittest
from task2.decrypt import decrypt
OutputOne = ['абра-кадабра.', 'абраа..-кадабра', 'абраа..-.кадабра', 'абра--..кадабра', 'абрау...-кадабра']
OutputEmpty = ['абра........', '.', '1.......................']

class TestDecrypt(unittest.TestCase):
    def test_then_get_word(self):
        for line in OutputOne:
            with self.subTest(line=line):
                self.assertEqual(decrypt(line), 'абра-кадабра')

    def test_then_get_empty(self):
        for line in OutputEmpty:
            with self.subTest(line=line):
                self.assertEqual(decrypt(line), '')

    def test_then_get_letter(self):
        self.assertEqual(decrypt('абр......a.'), 'a')

    def test_then_get_numbers(self):
        self.assertEqual(decrypt('1..2.3'), '23')