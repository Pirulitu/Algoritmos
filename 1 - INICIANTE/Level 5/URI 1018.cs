using System;

class URI1018
{
    static void Main(string[] args)
    {
            //troco
            int number = Int32.Parse(Console.ReadLine());
            Console.WriteLine(number);
            Console.WriteLine("{0} nota(s) de R$ 100,00",number/100);
            number = number % 100;
            Console.WriteLine("{0} nota(s) de R$ 50,00", number/50);
            number = number % 50;
            Console.WriteLine("{0} nota(s) de R$ 20,00",number/20);
            number = number % 20;
            Console.WriteLine("{0} nota(s) de R$ 10,00",number/10);
            number = number % 10;
            Console.WriteLine("{0} nota(s) de R$ 5,00",number/5);
            number = number % 5;
            Console.WriteLine("{0} nota(s) de R$ 2,00",number/2);
            number = number % 2;
            Console.WriteLine("{0} nota(s) de R$ 1,00",number/1);
    }

}