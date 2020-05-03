# 11.1.4

import unittest
from name_function3 import get_formatted_name3

class NamesTestCase3(unittest.TestCase):
    """测试 name_function3.py"""

    def test_first_last_name3(self):
        """能够正确地处理像 Janis Joplin 这样地姓名吗？"""
        formatted_name = get_formatted_name3('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

if __name__ == '__main__':
    unittest.main()
