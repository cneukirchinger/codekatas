import unittest
from chop import chop_walk

class TestChopMethod(unittest.TestCase):

    def test_chop_walk(self):
        self.assertEqual(-1, chop_walk(3, []))
        self.assertEqual(-1, chop_walk(3, [1]))
        self.assertEqual(0,  chop_walk(1, [1]))
        #
        self.assertEqual(0,  chop_walk(1, [1, 3, 5]))
        self.assertEqual(1,  chop_walk(3, [1, 3, 5]))
        self.assertEqual(2,  chop_walk(5, [1, 3, 5]))
        self.assertEqual(-1, chop_walk(0, [1, 3, 5]))
        self.assertEqual(-1, chop_walk(2, [1, 3, 5]))
        self.assertEqual(-1, chop_walk(4, [1, 3, 5]))
        self.assertEqual(-1, chop_walk(6, [1, 3, 5]))
        #
        self.assertEqual(0,  chop_walk(1, [1, 3, 5, 7]))
        self.assertEqual(1,  chop_walk(3, [1, 3, 5, 7]))
        self.assertEqual(2,  chop_walk(5, [1, 3, 5, 7]))
        self.assertEqual(3,  chop_walk(7, [1, 3, 5, 7]))
        self.assertEqual(-1, chop_walk(0, [1, 3, 5, 7]))
        self.assertEqual(-1, chop_walk(2, [1, 3, 5, 7]))
        self.assertEqual(-1, chop_walk(4, [1, 3, 5, 7]))
        self.assertEqual(-1, chop_walk(6, [1, 3, 5, 7]))
        self.assertEqual(-1, chop_walk(8, [1, 3, 5, 7]))

if __name__ == '__main__':
    unittest.main()
