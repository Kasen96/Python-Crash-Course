# 11-2

import unittest
from city_functions3 import get_formatted_city3

class CitiesTestCase3(unittest.TestCase):

    def test_city_country3(self):
        formatted_string = get_formatted_city3('santiago', 'chile')
        self.assertEqual(formatted_string, "Santiago, Chile")

    def test_city_country_population(self):
        formatted_string = get_formatted_city3('santiago', 'chile', 'population=5000000')
        self.assertEqual(formatted_string, "Santiago, Chile - population 5000000")

unittest.main()
