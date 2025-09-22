import unittest
from city_functions import get_city_country

class PopulationTestCase(unittest.TestCase):
    def test_population(self):
        full_name = get_city_country('nanyang', 'china', '9000000')
        self.assertEqual(full_name, "Nanyang, China - population 9000000")

unittest.main()