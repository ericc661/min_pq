using System;
namespace min_pq
{
    public static class HeapUtility
    {
        /* summary: given state of a heap, check each non-root node's
         *   parent priority is less than its priority
         * requires: heap to be the underlying array representing the heap,
         *   size to be the number of elements currently in the heap
         * effects: checks if array/heap preserves above property as well as
         *   ensures size is less than or equal to capacity. Throws an exception
         *   if either of these are not met.
         */
        public static void CheckInvariants(int[] heap, int size)
        {
            if (size > heap.Length)
            {
                throw new Exception("Heap size exceeds capacity.");
            }
            else
            {
                //don't check the root's parent as it has none
                int parent; //stores index of parent for current node
                for (int i=1; i<size; i++ )
                {
                    parent = (i - 1) / 2;
                    if (heap[parent] > heap[i])
                    {
                        throw new Exception("Heap property violated.");
                    }
                }
            }

        }

    }
}
