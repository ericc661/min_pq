/* Implementation of a simple minimum priority queue using a heap
 */

using System;
using System.Diagnostics;

namespace min_pq
{
    public class MinPriorityQueue
    {
        private int[] heap;
        private int size; // actual # elements in heap, differs from capacity
        
        /* summary: given state of underlying heap, check each non-root node's
         *   parent priority is less than its priority
         * requires: heap to be the underlying array representing the heap,
         *   size to be the number of elements currently in the heap
         * effects: checks if array/heap preserves above property as well as
         *   ensures size is less than or equal to capacity. Throws an exception
         *   if either of these are not met.
         */
        public void CheckInvariants(int[] heap, int size)
        {
            /*if (size > capacity)
            {
                throw new Exception("Heap size exceeds capacity");
            }
            else
            {
                //for (int i=0; i<this.size; )
            }*/
            throw new NotImplementedException();
        }

        // constructor
        public MinPriorityQueue(int capacity)
        {
            this.heap = new int[capacity];
            this.size = 0;
        }

        static void Main(string[] args)
        {
            MinPriorityQueue pq = new MinPriorityQueue(100);
            //Console.WriteLine(pq[0]);
        }
    }
}
