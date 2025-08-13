import unittest
from src.employee import Employee

class test_emp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('in set up class method')
        return super().setUpClass()
    
    def setUp(self):
        print('in set up method')
        self.emp1=Employee('Ram',20)
        self.emp1.update_mail('Dev',90)
    
    def tearDown(self):
        print('in tear down method')
    
    @classmethod
    def tearDownClass(cls):
        print('in tear down class method')
        return super().tearDownClass()
    
    def test_mail(self):
        print(self.emp1.mail)
        self.assertEqual(self.emp1.mail,'Ram@20.com')