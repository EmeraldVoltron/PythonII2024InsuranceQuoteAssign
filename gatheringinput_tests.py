"""
Abigail Boggs
amboggs@dmacc.edu
Last Edited: 1/11/24
Unit testing for Gathering input functions assignment
"""
import unittest
import unittest.mock as mock
import GatheringInputFunctionsAssignment as gi


class MyTestCase(unittest.TestCase):
    """
    IMPORTANT NOTE:
    If you are testing, you need to uncomment the "raise" lines in the 2 function's Except ValueError Blocks
    on GatheringInputFunctionsAssignment.py for the tests to run properly.
    This is because the program catches these exceptions with the try/except and re-asks for input from the user,
    resulting in an endless loop of death in the testing menu.
    If I put in side_effect with the values of 0 and 1, the tests will fail even though the first value entered
    raises the ValueError
    I'm not sure if there are other ways to avoid that, I spent a while looking up on the internet with no avail
    If you know a way, I'd love to hear feedback because this stumped me. I had no other idea of how to make the tests
    work without the comment idea.
    """
    def test_how_many_integers_less_than_1(self):
        # enter a 0 for this test
        with mock.patch('builtins.input', return_value = 0):
            self.assertRaises(ValueError, gi.how_many_integers)

    def test_how_many_integers_non_integer(self):
        # enter a 1.5 for this test
        with mock.patch('builtins.input', return_value="1.5"):
            self.assertRaises(ValueError, gi.how_many_integers)

    def test_integer_input_non_integer(self):
        # enter a 5.5 for this test
        with mock.patch('builtins.input', return_value="5.5"):
            self.assertRaises(ValueError, gi.integers_to_store, 1)


if __name__ == "__main__":
    unittest.main()
