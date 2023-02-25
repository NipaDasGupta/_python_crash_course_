import unittest
from city_function import get_formatted_string

class CityTestCase(unittest.TestCase):
    """Tests for 'city_function'."""

    def test_city_country(self):
        """Do values like 'Santiago, Chile' works?"""
        formatted_string = get_formatted_string('santiago', 'chile')
        self.assertEqual(formatted_string, 'Santiago, Chile')


    def test_city_country_population(self):
        """Do values like 'Santiago, Chile - population 5000000' works?"""
        formatted_string = get_formatted_string('santiago', 'chile', 5000000)
        self.assertEqual(formatted_string, 'Santiago, Chile - population 5000000')


if __name__ == '__main__':
    unittest.main()