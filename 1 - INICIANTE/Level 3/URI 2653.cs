using System;
using System.Collections;
using System.Linq;

class URI2653
{
    public static void Main(string[] args)
    {
        //problema simples de contar strings distintas
        //utilazando uma HashTable para ter acesso costante em buscar se a string ja foi vista
        string entrada;
        Hashtable save = new Hashtable();
        int count = 0;
        while (!string.IsNullOrEmpty(entrada = Console.ReadLine()) && entrada != "")    
        {
            if(save.Contains(entrada))
                continue;
            save.Add(entrada,0);
            count++;
        }
        Console.WriteLine(count);

    }
}