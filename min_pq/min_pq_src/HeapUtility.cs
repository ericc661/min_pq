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
                //for (int i=0; i<this.size; )
            }
            throw new NotImplementedException();
        }
    }
}
