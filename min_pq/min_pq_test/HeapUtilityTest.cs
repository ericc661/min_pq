using Microsoft.VisualStudio.TestTools.UnitTesting;
using System;

namespace min_pq
{
    [TestClass]
    public class HeapUtilityTest
    {
        //private int[] heap1;
        //private int size1;

        [TestInitialize]
        public void InitTestState()
        {
            
            
        }

        /* Tests for CheckInvariants: partition along size/capacity of heap
         *   (0, 1, etc.) as well as which invariant is violated/preserved:
         *   size vs. capacity and heap property
         */

        //basic test to ensure exception thrown upon size > capacity
        [TestMethod]
        [ExpectedException(typeof(Exception), "Heap size exceeds capacity.")]
        public void TestCheckInvariants1()
        {
            int[] heap = new int[5];
            HeapUtility.CheckInvariants(heap, 6);
        }

        //empty heap, nothing should happen
        [TestMethod]
        public void TestCheckInvariants2()
        {
            int[] heap = new int[0];
            HeapUtility.CheckInvariants(heap, 0);
        }

        //heap of size 1, nothing should happen
        [TestMethod]
        public void TestCheckInvariants3()
        {
            int[] heap = new int[5];
            heap[0] = 10;
            HeapUtility.CheckInvariants(heap, 1);
        }

        //correct heap of size 8, no exceptions should be thrown
        [TestMethod]
        public void TestCheckInvariants4()
        {
            int[] heap = new int[10];
            int[] values = { 5, 10, 9, 11, 13, 12 };
            for(int i=0; i<values.Length; i++)
            {
                heap[i] = values[i];
            }

            HeapUtility.CheckInvariants(heap, values.Length);
        }

        //heap of size 6 that violates heap property
        [TestMethod]
        [ExpectedException(typeof(Exception), "Heap property violated.")]
        public void TestCheckInvariants5()
        {
            int[] heap = new int[10];
            int[] values = { 5, 7, 9, 8, 3, 10 };
            for (int i = 0; i < values.Length; i++)
            {
                heap[i] = values[i];
            }

            HeapUtility.CheckInvariants(heap, values.Length);
        }


    }
}
