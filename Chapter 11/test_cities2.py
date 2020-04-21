# 11-2

import unittest
from city_functions2 import get_formatted_city2

class CitiesTestCase2(unittest.TestCase):

    def test_city_country2(self):
        formatted_string = get_formatted_city2('santiago', 'chile')
        self.assertEqual(formatted_string, "Santiago, Chile")

unittest.main()
