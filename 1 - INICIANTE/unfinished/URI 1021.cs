using System;
using System.Linq;

class URI1021
{
        static void Main(string[] args)
        {
            //troco
            string nStr = Console.ReadLine();
            int[] num = nStr.Split('.').Select(Int32.Parse).ToArray();
            int nota = num[0], moeda = num[1];
            Console.WriteLine("NOTAS:");
            Console.WriteLine("{0} nota(s) de R$ 100,00", nota/100);
            nota = nota % 100;
            Console.WriteLine("{0} nota(s) de R$ 50,00", nota /50);
            nota = nota % 50;
            Console.WriteLine("{0} nota(s) de R$ 20,00", nota /20);
            nota = nota % 20;
            Console.WriteLine("{0} nota(s) de R$ 10,00", nota /10);
            nota = nota % 10;
            Console.WriteLine("{0} nota(s) de R$ 5,00", nota /5);
            nota = nota % 5;
            Console.WriteLine("{0} nota(s) de R$ 2,00", nota /2);
            nota = nota % 2;

            Console.WriteLine("MOEDAS:");

            Console.WriteLine("{0} moeda(s) de R$ 1.00",nota/1);

            Console.WriteLine("{0} moeda(s) de R$ 0.50", moeda / 50);
            moeda %= 50;
            Console.WriteLine("{0} moeda(s) de R$ 0.25", moeda / 25);
            moeda %= 25;
            Console.WriteLine("{0} moeda(s) de R$ 0.10", moeda / 10);
            moeda %= 10;
            Console.WriteLine("{0} moeda(s) de R$ 0.05", moeda / 5);
            moeda %= 5;
            Console.WriteLine("{0} moeda(s) de R$ 0.01", moeda / 1);
        }
}
