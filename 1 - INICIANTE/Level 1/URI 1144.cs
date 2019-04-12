using System;

class URI1144
{
    //sequencia de intervalo n imprimindo o quadrado e o cubo e quadrado e cubo +1
    static void Main(string[] args)
    {
        int n = Int32.Parse(Console.ReadLine());
        for (int i = 1; i <= n; i++)
        {
            long nquadrado = (int)Math.Pow(i, 2);
            long ncubo = (int)Math.Pow(i, 3);
            System.Console.WriteLine("{0} {1} {2}", i, nquadrado, ncubo);
            System.Console.WriteLine("{0} {1} {2}", i, nquadrado + 1, ncubo + 1);
        }
    }

}