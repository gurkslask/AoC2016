import unittest
import solver


class TestSolver(unittest.TestCase):
    def test_checker(self):
        self.assertEqual(solver.checker('aaaaa-bbb-z-y-x-123[abxyz]'), 123)
        self.assertEqual(solver.checker('a-b-c-d-e-f-g-h-987[abcde]'), 987)
        self.assertEqual(solver.checker('totally-real-room-200[decoy]'), 0)

    def test_solver(self):
        self.assertEqual(solver.solver([
            'aaaaa-bbb-z-y-x-123[abxyz]',
            'a-b-c-d-e-f-g-h-987[abcde]',
            'totally-real-room-200[decoy]',
            'not-a-real-room-404[oarel]',
        ]), 1514)

    def test_splitter(self):
        self.assertEqual(solver.splitter(
            'aaaaa-bbb-z-y-x-123[abxyz]'),
            ['aaaaabbbzyx', 123, 'abxyz'])

if __name__ == '__main__':
    unittest.main()
