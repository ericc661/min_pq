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
