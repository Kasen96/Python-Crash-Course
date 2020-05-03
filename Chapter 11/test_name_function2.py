# 11.1.3

import unittest
from name_function2 import get_formatted_name2

class NamesTestCase2(unittest.TestCase):
    """测试 name_function2.py"""

    def test_first_last_name2(self):
        """能够正确地处理像 Janis Joplin 这样地姓名吗？"""
        formatted_name = get_formatted_name2('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

if __name__ == '__main__':
    unittest.main()
