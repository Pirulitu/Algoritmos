using System;
using System.Linq;

    class URI1161
    {
        static void Main(string[] args)
        {
            string input;
            while (!String.IsNullOrEmpty(input=Console.ReadLine()) && input != "")
            {
                int[] numbers = input.Split(' ').Select(Int32.Parse).ToArray();
                int n1 = numbers[0];
                int n2 = numbers[1];
                Console.WriteLine(fatorial(n1)+fatorial(n2));
            }
        }

        public static long fatorial(int n)
        {
            if (n <= 1)
                return 1;
            else
                return n * fatorial(n - 1);
        }
    }