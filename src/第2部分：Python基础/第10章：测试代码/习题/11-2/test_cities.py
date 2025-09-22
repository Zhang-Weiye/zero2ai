import unittest
from city_functions import get_city_country

class CityCountryTestCase(unittest.TestCase):
    def test_city_country(self):
        full_name = get_city_country('shanghai', 'china')
        self.assertEqual(full_name, 'Shanghai, China')

unittest.main()