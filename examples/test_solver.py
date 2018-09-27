from unittest import TestCase
from some_random_program import Solver

class TestSolver(TestCase):
    def test_negative_disc(self):
        s = Solver()
        self.assertRaises(Exception, s.demo(2, 1, 1))

    def test_demo(self):
        self.fail()
