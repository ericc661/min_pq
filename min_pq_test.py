import unittest
from min_pq import min_PQ

class test_check_invariant(unittest.TestCase):

    # emtpy heap case, should not raise error
    def test1(self):
        pq = min_PQ()
        try:
            pq.check_invariant()
        except RuntimeError:
            self.fail('Unexpected - heap invariant violated')

    # size 1 case should also not raise error
    def test2(self):
        pq = min_PQ()
        pq.heap = [68]
        try:
            pq.check_invariant()
        except RuntimeError:
            self.fail('Unexpected - heap invariant violated')

    # invalid heap, should raise error
    def test3(self):
        pq = min_PQ()
        pq.heap = [2, 3, 5, 4, 1, 6]
        self.assertRaises(RuntimeError, pq.check_invariant)

    # valid heap, should not raise error
    def test4(self):
        pq = min_PQ()
        pq.heap = [1, 2, 3, 4, 5, 6, 7]
        try:
            pq.check_invariant()
        except RuntimeError():
            self.fail('Unexpected - heap invariant violated')

class test_insert(unittest.TestCase):

    # trivial case
    def test1(self):
        pq = min_PQ()
        pq.insert(10)
        self.assertEqual(len(pq.heap), 1)
        self.assertEqual(pq.heap, [10])

    # also sort of trivial
    def test2(self):
        pq = min_PQ()
        pq.heap = [5]
        pq.insert(7)
        self.assertEqual(len(pq.heap), 2)
        self.assertEqual(pq.heap, [5, 7])

    # inserting a new minimum priority
    def test3(self):
        pq = min_PQ()
        pq.heap = [2, 5, 7, 8, 9]
        pq.insert(1)
        self.assertEqual(len(pq.heap), 6)
        self.assertEqual(pq.heap, [1, 5, 2, 8, 9, 7])

    # inserting a priority that ends up somewhere in the middle
    def test4(self):
        pq = min_PQ()
        pq.heap = [5, 8, 11, 13, 14, 12, 17, 19]
        pq.insert(10)
        self.assertEqual(len(pq.heap), 9)
        self.assertEqual(pq.heap, [5, 8, 11, 10, 14, 12, 17, 19, 13])

if __name__ == '__main__':
    unittest.main()
