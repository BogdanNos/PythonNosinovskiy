import unittest
import calculate

class TestSalary(unittest.TestCase):
    def setUp(self):
        calculate.app.config['TESTING'] = True
        calculate.app.config['DEBUG'] = False
        calculate.salary = {2020: {10: 200, 11: 100}, 2003: {12: 500}}
        self.app = calculate.app.test_client()

    def test_can_add_salary(self):
        response = self.app.get('/add/20221012/500')
        response_text = response.data.decode()
        self.assertTrue('Добавлена информация о трате' in response_text)

    def test_can_add_salary_to_calculate(self):
        self.app.get('/add/20111013/1000')
        response = self.app.get('/calculate/2011/10')
        response_text = response.data.decode()
        self.assertTrue('1000' in response_text)

    def test_can_add_get_invalid_date(self):
        response = self.app.get('/add/sdhkschsc/1000')
        response_text = response.data.decode()
        self.assertTrue('Неверный ввод' in response_text)

    def test_can_calculate_salary_by_year(self):
        response = self.app.get('/calculate/2020')
        response_text = response.data.decode()
        self.assertTrue('300' in response_text)

    def test_can_calculate_empty_salary_by_year(self):
        response = self.app.get('/calculate/2015')
        response_text = response.data.decode()
        self.assertTrue('За данный год не было покупок' in response_text)

    def test_can_calculate_salary_function_get_by_year(self):
        self.assertEqual('300', calculate.calculateYear(2020))

    def test_can_calculate_salary_by_year_and_month(self):
        response = self.app.get('/calculate/2003/12')
        response_text = response.data.decode()
        self.assertTrue('500' in response_text)

    def test_can_calculate_empty_salary_by_month(self):
        response = self.app.get('/calculate/2015/12')
        response_text = response.data.decode()
        self.assertTrue('За данный месяц не было покупок' in response_text)

    def test_can_calculate_salary_function_get_by_month(self):
        self.assertEqual('200', calculate.calculateMounth(2020, 10))