
class min_PQ(object):
    def __init__(self):
        self.heap = []

    def __repr__(self):
        heap_string = ''
        for i in range(len(self.heap)):
            heap_string += str(self.heap[i]) + ' '
        return heap_string

    # check each non-root node is >= its parent
    def check_invariant(self):
        #emtpy and 1-size heaps cannot violate heap property
        if len(self.heap)>1:
            for i in range(1, len(self.heap)):
                if self.heap[(i-1) // 2] > self.heap[i]:
                    raise RuntimeError('Heap invariant violated')

    # utility function to swap two indices in the heap (not tested)
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

    def is_empty(self):
        return len(self.heap) == 0

    # summary: returns item with minimum priority and removes it from PQ
    # requires: is_empty to be checked before calling
    # effects: IndexError if called on an empty PQ. Otherwise, removes minimum
    #   item and returns it, replacing it with last item in PQ. "bubbles down"
    #   if needed.
    def remove_min(self):
        min_priority = self.heap[0]
        self.swap(0, len(self.heap)-1) #bring last element to front
        self.heap.pop() #remove last element, which was the min

        #bubble down
        i_current = 0
        next_swap = self.next_down(i_current)
        while (next_swap != None): #while we should swap
            self.swap(i_current, next_swap) #swap the elements
            i_current = next_swap #i_current is now in the place of one of its children
            next_swap = self.next_down(i_current)

        return min_priority

    # summary: given an index representing a priority we are bubbling down,
    #   returns index of node it should be swapped with.
    # requires: index of item of interest
    # effects: if node has no children (leaf) or the minimum of its children
    #   is strictly greater than it, then return None. Otherwise, return
    #   the index of the minimum-priority child
    def next_down(self, i):
        max_ind = len(self.heap)-1 #get max index of current heap
        left = (2*i) + 1 #calculate where left and right child would be
        right = left + 1
        if left > max_ind: #if this is true, node is a leaf
            return None
        elif right > max_ind: #node has left child but not right
            if self.heap[left] < self.heap[i]:
                return left
            else:
                return None
        else: #both children exist
            next = None #default if we cannot find a suitable node to swap with
            if self.heap[left] < self.heap[i]: #left child might need to be swapped
                next = left
            if self.heap[right] < self.heap[left]: #overwrite if right is actually smaller
                next = right
            return next


def main():
    pq = min_PQ()
    print(pq)

if __name__ == '__main__':
    main()
