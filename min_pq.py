
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

    # utility function to swap two indices in the heap
    def swap(self, i, j):
        old_i = self.heap[i] # store old value at index i
        self.heap[i] = self.heap[j]
        self.heap[j] = old_i

    # inserts given priority into end of heap then "bubbles up" until
    #   invariant is preserved
    def insert(self, priority):
        self.heap.append(priority)
        i_new = len(self.heap)-1 # get location of just-inserted priority
        i_parent = (i_new-1) // 2 # get location of its parent

        # "bubble up" step
        while (i_new > 0) and (self.heap[i_parent] > self.heap[i_new]):
            self.swap(i_new, i_parent)
            i_new = i_parent # after swap: newly inserted priority gets loc of parent
            i_parent = (i_parent-1) // 2

        self.check_invariant() #check invariant after bubbling up

def main():
    pq = min_PQ()
    print(pq)

if __name__ == '__main__':
    main()
