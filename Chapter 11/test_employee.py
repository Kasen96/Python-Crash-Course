# 11-3

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.employee = Employee('a', 'b', 1000)
    
    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(6000, self.employee.wage)

    def test_give_custom_raise(self):
        self.employee.give_raise(2000)
        self.assertEqual(3000, self.employee.wage)

unittest.main()
