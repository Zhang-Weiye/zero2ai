import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee('king', 'domdom', 1000000)
        self.salary = 1000000
        self.increment = 100000

    def test_give_default_raise(self):
        self.assertEqual(self.salary, self.employee.salary)

    def test_give_custom_raise(self):
        self.employee.give_raise(self.increment)
        self.assertEqual(self.employee.salary, self.salary + self.increment)

unittest.main()