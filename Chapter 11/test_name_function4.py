# 11.1.5

import unittest
from name_function3 import get_formatted_name3

class NamesTestCase4(unittest.TestCase):
    """测试 name_function3.py"""

    def test_first_last_name4(self):
        """能够正确地处理像 Janis Joplin 这样地姓名吗？"""
        formatted_name = get_formatted_name3('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """能够正确地处理像 Wolfgang Amadeus Mozart 这样的名字吗？"""
        formatted_name = get_formatted_name3('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

if __name__ == '__main__':
    unittest.main()
