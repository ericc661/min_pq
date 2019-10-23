using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace min_pq
{
    [TestClass]
    public class MinPQTest
    {
        private int[] heap1;
        private int size1;

        [TestInitialize]
        public void InitTestState()
        {
            heap1 = new int[100];
            MinPriorityQueue pq = new MinPriorityQueue(100);
        }

        [TestMethod]
        public void TestMethod1()
        {
            Assert.AreEqual(1, 1);
        }
    }
}
