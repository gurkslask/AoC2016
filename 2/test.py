import unittest
import solver


class TestSolver(unittest.TestCase):
    def test_solver(self):
        self.assertEqual(solver.solver([['U', 'U', 'U', 'U', 'U'], ['L'], ['U', 'L', 'R', 'D']]), [2, 4, 5])

if __name__ == '__main__':
    unittest.main()
