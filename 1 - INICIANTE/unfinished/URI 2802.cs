using System;

class URI2802
{
    public static void Main(string[] args)
    {    
        //calcular o fatorial para N maior que 20 ta passando de 64 bits pro inteiro
        ulong n = ulong.Parse(Console.ReadLine());

        ulong comb_n_2 = (fatorial(n) / (fatorial(n - 2) * fatorial(2)));
        ulong comb_n_4 = (fatorial(n) / (fatorial(n - 4) * fatorial(4)));
        ulong res = 1 + comb_n_2 + comb_n_4 ;
        Console.WriteLine(res);
    }

    public static ulong fatorial(ulong n)
    {
        if (n <= 1)
            return 1;
        else
            return n * fatorial(n - 1);

    }
}