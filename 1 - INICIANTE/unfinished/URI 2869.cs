using System;

namespace Algoritmos
{
    class Problema2869
    {
        static void Main(string[] args)
        {
            int [] nDivisores = new int[101];
            nDivisores[0] = 0;
            nDivisores[1] = 1;

            int n = 2, max = 2;
            while (n < 100)
            {
                Console.WriteLine("{0} {1}",n, max);
                int count = 2;
                int maxN = max;
                while (maxN % 2 == 0)
                {
                    maxN = maxN / 2;
                    if (maxN > 1)
                        break;


                }
                for (int i = 2; i <= Math.Floor(Math.Sqrt(max))+1; i++)
                {
                    if (max % i == 0 )
                    {
                        count++;
                        if (max/i != i)
                            count++;
                    }
                }

                if (count <= 100 && nDivisores[count] == 0)
                {
                    nDivisores[count] = max;
                    n++;
                }

                max++;
            }

            int m = 0;
            foreach (int elemento in nDivisores)
            {
                Console.WriteLine("{0} {1}",m,elemento);
                m++;
            }

        }
    }
}
