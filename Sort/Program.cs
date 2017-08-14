using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading;
using System.Diagnostics;

namespace Sort
{
    class Program
    {
        static void Main(string[] args)
        {
            Stopwatch stopWatch = new Stopwatch();

            int[] MasterIntegerArray = ExampleData.Data_1000;

            int[] result;

            bool show = false;

            Methods _Methods = new Methods();

            stopWatch.Start();
            result = _Methods.VisualSort(MasterIntegerArray);
            stopWatch.Stop();
            Console.WriteLine("VisualSort");
            if (show) DisplayArray(result);
            Console.WriteLine("Time elapsed: {0}", stopWatch.Elapsed);
            Console.WriteLine();


            stopWatch.Reset();
            stopWatch.Start();
            result = _Methods.SelectionSort(MasterIntegerArray);
            stopWatch.Stop();
            Console.WriteLine("SelectionSort");
            if (show) DisplayArray(result);
            Console.WriteLine("Time elapsed: {0}", stopWatch.Elapsed);
            Console.WriteLine();


            stopWatch.Reset();
            stopWatch.Start();
            result = _Methods.BubbleSort(MasterIntegerArray);
            stopWatch.Stop();
            Console.WriteLine("BubbleSort");
            if (show) DisplayArray(result);
            Console.WriteLine("Time elapsed: {0}", stopWatch.Elapsed);
            Console.WriteLine();


            stopWatch.Reset();
            stopWatch.Start();
            result = _Methods.InsertionSort(MasterIntegerArray);
            stopWatch.Stop();
            Console.WriteLine("InsertionSort");
            if (show) DisplayArray(result);
            Console.WriteLine("Time elapsed: {0}", stopWatch.Elapsed);
            Console.WriteLine();


            stopWatch.Reset();
            stopWatch.Start();
            result = _Methods.MergeSort(MasterIntegerArray);
            stopWatch.Stop();
            Console.WriteLine("MergeSort");
            if (show) DisplayArray(result);
            Console.WriteLine("Time elapsed: {0}", stopWatch.Elapsed);
            Console.WriteLine();


            stopWatch.Reset();
            stopWatch.Start();
            int[] QuickSortedMasterIntegerArray = MasterIntegerArray.ToArray();
            _Methods.QuickSort(QuickSortedMasterIntegerArray, 0 , QuickSortedMasterIntegerArray.Length - 1);
            stopWatch.Stop();
            Console.WriteLine("QuickSort");
            if (show) DisplayArray(QuickSortedMasterIntegerArray);
            Console.WriteLine("Time elapsed: {0}", stopWatch.Elapsed);
            Console.WriteLine();

            Console.Read();
        }

        static void DisplayArray(int[] Array)
        {
            Console.Write("[ ");
            foreach (var item in Array)
            {
                Console.Write("{0}, ", item);
            }
            Console.WriteLine("]");
        }

    }
}
