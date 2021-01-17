from unittest import TestCase
from unittest.mock import patch
from src.db_helper import DbHelper

class TestDBHelper(TestCase):
    def setUp(self):
        self.dbHelper = DbHelper()

    '''
    def test_salary_without_mocking(self):
        actual_max = self.dbHelper.get_maximum_salary()
        actual_min = self.dbHelper.get_minimum_salary()
        self.assertGreater(actual_max,actual_min)
    '''  

    @patch('src.db_helper.DbHelper')
    def test_salary_with_mocking(self, MockSalary):
        # create a mock object of DbHelper class. This will help to customize output of class methods
        self.dbHelper = MockSalary()
        
        #mocked the return values of methods
        self.dbHelper.get_maximum_salary.return_value = 40000
        self.dbHelper.get_minimum_salary.return_value = 30000

        #variables 'actual_max' and 'actual_min' will get values from mocked version
        actual_max = self.dbHelper.get_maximum_salary()
        actual_min = self.dbHelper.get_minimum_salary()
        
        self.assertGreater(actual_max,actual_min)
        