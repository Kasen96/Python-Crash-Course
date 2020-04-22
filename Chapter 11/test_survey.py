# 11.2.3

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """针对 AnonymousSurvey 类的测试"""

    def test_store_single_response(self):
        """测试单个答案会被妥善地存储""" 
        question = "What language did you first learn to speak?" 
        my_survey = AnonymousSurvey(question) 
        my_survey.store_response('English')

        self.assertIn('English', my_survey.responses)

unittest.main()
