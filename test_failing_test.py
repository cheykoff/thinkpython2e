import empty_module
import unittest


class FirstTestClass(unittest.TestCase):
    """a failing test for a new module"""
    result = 1

    def test_first_test_method(self):
        first = self.result
        second = empty_module.empty_function()
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
