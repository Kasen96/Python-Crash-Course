# 11.2.3

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey2(unittest.TestCase):
    """针对 AnonymousSurvey 类的测试"""

    def test_store_single_response2(self):
        """测试单个答案会被妥善地存储""" 
        question = "What language did you first learn to speak?" 
        my_survey = AnonymousSurvey(question) 
        my_survey.store_response('English')

        self.assertIn('English', my_survey.responses)

    def test_store_three_response2(self):
        """测试三个答案会被妥善地存储"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response, my_survey.responses)

if __name__ == '__main__':
    unittest.main()
