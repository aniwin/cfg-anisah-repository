import unittest

from squared import squared_function


class MyTestCase(unittest.TestCase):
    def test_squared(self):
        expected = [1, 4, 9, 25, 36, 64, 81]
        actual = squared_function([1,2,3,5,6,8,9])
        self.assertEqual(actual, expected)

    def test_string_input(self):
        with self.assertRaises(TypeError):
            squared_function('asdf')


if __name__ == '__main__':
    unittest.main()

# first test case tests if function returns the expected output
# second test case tests if the function returns an invalid error if wrong input is entered
