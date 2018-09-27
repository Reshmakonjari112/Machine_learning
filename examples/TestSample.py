import unittest
from some_random_program import Solver

class MyTestCase(unittest.TestCase):
    def test_negative_disc(self):
        s = Solver()
        self.assertRaises(Exception, s.demo(2, 1, 2))

    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
