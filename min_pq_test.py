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

if __name__ == '__main__':
    unittest.main()
