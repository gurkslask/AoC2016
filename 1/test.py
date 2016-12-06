import unittest
import solver


class TestSolution(unittest.TestCase):
    def test_countdist(self):
        self.assertEqual(solver.countdistance([2, 10]), 12)

    def test_parse(self):
        self.assertEqual(solver.parseinput(['R2', 'L4', 'L444']), [['R', 2], ['L', 4], ['L', 444]])

    def test_walk(self):
        self.assertEqual(solver.walk([['R', 2], ['L', 3]]), [3, 2])
        self.assertEqual(solver.walk([['R', 2], ['R', 2], ['R', 2]]), [-2, 0])
        self.assertEqual(solver.walk([['R', 5], ['L', 5], ['R', 5], ['R', 3]]), [2, 10])

if __name__ == '__main__':
    unittest.main()
