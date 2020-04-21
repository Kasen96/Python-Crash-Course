# 11-1

import unittest
from city_functions import get_formatted_city

class CitiesTestCase(unittest.TestCase):

    def test_city_country(self):
        formatted_string = get_formatted_city('santiago', 'chile')
        self.assertEqual(formatted_string, "Santiago, Chile")

unittest.main()
