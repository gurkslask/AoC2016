import unittest
import solver


class TestSolver(unittest.TestCase):
    def test_checker(self):
        self.assertEqual(solver.checker('abba'), True)
        self.assertEqual(solver.checker('abda'), False)
        self.assertEqual(solver.checker('abcdefghi'), False)
        self.assertEqual(solver.checker('abcderfgjkaddangfhalengfja'), True)
        self.assertEqual(solver.checker('aaaa'), False)

    def test_splitter(self):
        self.assertEqual(solver.splitter('aaaa[baaa]caaa[dcd]ghg'), {'good': ['aaaa', 'caaa', 'ghg'], 'bad': ['baaa', 'dcd']})
        self.assertEqual(solver.splitter('aaaa[baaa]caaa'), {'good': ['aaaa', 'caaa'], 'bad': ['baaa']})
        self.assertEqual(solver.splitter('a[b]c'), {'good': ['a', 'c'], 'bad': ['b']})

    def test_solver(self):
        self.assertEqual(solver.solver(['abba[dcaa]mkjh', 'abba[abba]dsad']), 1)

if __name__ == '__main__':
    unittest.main()
