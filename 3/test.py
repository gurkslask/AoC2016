import unittest
import solver


class TestSolver(unittest.TestCase):
    def test_checker(self):
        self.assertEqual(solver.checker([5, 10, 25]), False)
        self.assertEqual(solver.checker([10, 25, 5]), False)
        self.assertEqual(solver.checker([25, 5, 10]), False)
        self.assertEqual(solver.checker([1, 1, 1]), True)

    def test_solver(self):
        self.assertEqual(solver.solver([
            '1 1 1',
            '5 10 25',
            '2 4 5',
            '25 10 5',
            '300 300 300',
            '1200 300 300',
            '120 400 300'
            ]), 4)

    def test_splitter(self):
        self.assertEqual(solver.splitter('   8  234  831'), [8, 234, 831])
        self.assertEqual(solver.splitter('  175   40  994'), [175, 40, 994])

if __name__ == '__main__':
    unittest.main()
