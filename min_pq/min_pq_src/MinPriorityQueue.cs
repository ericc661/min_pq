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
        
        //TODO: make public properties for testing?

        // constructor
        public MinPriorityQueue(int capacity)
        {
            this.heap = new int[capacity];
            this.size = 0;
        }

        /* summary: inserts new element and changes heap to preserve heap
         *   invariants.
         * requires: priority to be the priority of the item to be inserted
         * effects: throws an exception if heap is full. Otherwise, increments
         *   size of the heap, inserts item into last position, and "bubbles up"
         *   until heap property is satisfied.
         */
        public void Insert(int priority)
        {
            throw new NotImplementedException();
        }

        static void Main(string[] args)
        {
            MinPriorityQueue pq = new MinPriorityQueue(100);
            //Console.WriteLine(pq[0]);
        }


    }
}
