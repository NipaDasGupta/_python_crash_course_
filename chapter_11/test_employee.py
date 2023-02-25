import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    """Tests for the class Employee."""

    def setUp(self):
        """Create a new employee and a set of cases in all the test methods."""
        self.new_employee = Employee('nipa', 'das gupta', 5000)
        self.default_raise = self.new_employee.give_rise()
        self.custom_raise = self.new_employee.give_rise(8000)

    def test_give_default(self):
        """Test that for a given default annual salary of an employee."""
        self.assertEqual(5000, self.default_raise)

    def test_give_custom_raise(self):
        """Test that for a given custom annual salary of an employee."""
        self.assertEqual(8000, self.custom_raise)


if __name__ == '__main__':
    unittest.main()
