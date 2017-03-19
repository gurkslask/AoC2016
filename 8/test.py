import unittest
from solver import Panel


class TestSolver(unittest.TestCase):
    def setUp(self):
        self.P = Panel(3, 3)

    def test_checker(self):
        self.assertEqual(self.P.counter(), 0)


if __name__ == '__main__':
    unittest.main()
