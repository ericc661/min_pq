
class min_PQ(object):
    def __init__(self):
        self.heap = []

    def __repr__(self):
        heap_string = ''
        for i in range(len(self.heap)):
            heap_string += str(self.heap[i]) + ' '
        heap_string += str(len(self.heap))
        return heap_string

    # check each non-root node is >= its parent
    def check_invariant(self):
        #emtpy and 1-size heaps cannot violate heap property
        if len(self.heap)>1:
            for i in range(1, len(self.heap)):
                if self.heap[(i-1) // 2] > self.heap[i]:
                    raise RuntimeError('Heap invariant violated')


def main():
    print('what am i doing lmao')
    pq = min_PQ()
    print(pq)

if __name__ == '__main__':
    main()
