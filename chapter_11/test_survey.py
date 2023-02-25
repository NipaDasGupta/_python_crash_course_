import unittest
from survey import AnonymousSurvey


# class TestAnonymousSurvey(unittest.TestCase):
#     """Tests for the class AnonymousSurvey."""

#     def test_store_single_response(self):
#         """Test that a single response is store properly."""
#         question = "What language did you first learn to speak?"
#         my_survey = AnonymousSurvey(question)
#         my_survey.store_response("Bangla")
#         self.assertIn('Bangla', my_survey.responses)

#     def test_store_three_response(self):
#         """Test that a three individual response is store properly."""
#         question = "What language did you first learn to speak?"
#         my_survey = AnonymousSurvey(question)
#         responses = ['Bangla', 'English', 'Hindi']

#         for response in responses:
#             my_survey.store_response(response)

#         for response in responses:
#             self.assertIn(response, my_survey.responses)


class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey."""

    def setUp(self):
        """
        Create a survey and a set of responses for use in all test methods.
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['Bangla', 'English', 'Hindi']

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


if __name__ == '__main__':
    unittest.main()
