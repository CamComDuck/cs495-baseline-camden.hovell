import unittest
import utils

class TestStringMethods(unittest.TestCase):

    def test_letters(self):
        test_string = 'aaaaaaaaaaeioua'
        result = utils.UniqueChars.first_unique_char(test_string)
        self.assertEqual(result, 10)

    def test_numbers(self):
        test_string = '11231'
        result = utils.UniqueChars.first_unique_char(test_string)
        self.assertEqual(result, 2)

    def test_all_repeat(self):
        test_string = 'aaaaa'
        result = utils.UniqueChars.first_unique_char(test_string)
        self.assertEqual(result, -1)

    def test_failing(self):
        test_string = 'aaaaa'
        result = utils.UniqueChars.first_unique_char(test_string)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()