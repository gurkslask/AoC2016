import sys
sys.path.append('..')
import unittest
from solver import solver


class TestSolver(unittest.TestCase):
    def test_solver(self):
        self.assertEqual(solver(['aabc', 'bbbc']), ['a', 'b'])


if __name__ == '__main__':
    unittest.main()
