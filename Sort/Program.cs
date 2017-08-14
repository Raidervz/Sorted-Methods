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

            int[] MasterIntegerArray = new int[] { 8, 4, 6, 188, 4, 6, 8, 9, 15, 45,  2};

            int[] result;

            Methods _Methods = new Methods();

            Console.WriteLine();
            Console.Write("Sorted By Visual:    [ ");
            stopWatch.Start();
            result = _Methods.VisualSort(MasterIntegerArray);
            stopWatch.Stop();
            foreach (var item in result)
            {
                Console.Write("{0}, ", item);
            }
            Console.WriteLine("]");
            Console.WriteLine("Time elapsed: {0}", stopWatch.Elapsed);
            Console.WriteLine();


            stopWatch.Reset();
            Console.WriteLine();
            stopWatch.Start();
            result = _Methods.SelectionSort(MasterIntegerArray);
            stopWatch.Stop();
            Console.Write("Sorted By Selection: [ ");
            foreach (var item in result)
            {
                Console.Write("{0}, ", item);
            }
            Console.WriteLine("]");
            Console.WriteLine("Time elapsed: {0}", stopWatch.Elapsed);
            Console.WriteLine();


            stopWatch.Reset();
            Console.WriteLine();
            stopWatch.Start();
            result = _Methods.BubbleSort(MasterIntegerArray);
            stopWatch.Stop();
            Console.Write("Sorted By BubbleSort: [ ");
            foreach (var item in result)
            {
                Console.Write("{0}, ", item);
            }
            Console.WriteLine("]");
            Console.WriteLine("Time elapsed: {0}", stopWatch.Elapsed);
            Console.WriteLine();


            stopWatch.Reset();
            Console.WriteLine();
            stopWatch.Start();
            result = _Methods.InsertionSort(MasterIntegerArray);
            stopWatch.Stop();
            Console.Write("Sorted By InsertionSort: [ ");
            foreach (var item in result)
            {
                Console.Write("{0}, ", item);
            }
            Console.WriteLine("]");
            Console.WriteLine("Time elapsed: {0}", stopWatch.Elapsed);
            Console.WriteLine();


            stopWatch.Reset();
            Console.WriteLine();
            stopWatch.Start();
            result = _Methods.MergeSort(MasterIntegerArray);
            stopWatch.Stop();
            Console.Write("Sorted By MergeSort: [ ");
            foreach (var item in result)
            {
                Console.Write("{0}, ", item);
            }
            Console.WriteLine("]");
            Console.WriteLine("Time elapsed: {0}", stopWatch.Elapsed);
            Console.WriteLine();


            Console.Read();
        }

    }
}
