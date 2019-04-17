using System;
using System.Collections;

class URI2674
{
    public static void Main(string[] args)
    {

        Hashtable primos =  crivo(1000000);

        string entrada;

        while (!String.IsNullOrEmpty(entrada = Console.ReadLine()) && entrada != "")//while not EOF
        {
            int n = Int32.Parse(entrada);
            bool estado = true;
            if (primos.Contains(n))
            {
                char [] numero = entrada.ToCharArray();
                for (int i = 0; i < numero.Length; i++)
                    if (!primos.Contains(Int32.Parse(numero[i].ToString())))
                    {
                        Console.WriteLine("Primo");
                        estado = false;
                        break;
                    }

                if (estado)
                    Console.WriteLine("Super");
            }
            else
                Console.WriteLine("Nada");
        }
    }

    public static Hashtable crivo (int max)//crivo de eratóstenes
    {
        int sqrtMax = (int)Math.Sqrt(max)+1;
        
        Hashtable primos = new Hashtable();

        primos.Add(2,2);//adiciona 2 como primo
        for (int i = 3; i < max; i+=2)
        //inicialmente adiciona todos numeros impares como primo
            primos.Add(i,i);
        
        for (int i = 3; i <= sqrtMax; i+=2)//remove todos multiplos de i
            if (primos.Contains(i))
                for (int j = i+i; j < max; j+=i)
                    primos.Remove(j);
        return primos;
    }
}
