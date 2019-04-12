using System;
using System.Linq;
using System.Text;
class URI1026
{
    static void Main(string[] args)
    {
        string entrada;
        while (!String.IsNullOrEmpty(entrada = Console.ReadLine()) && entrada != "")
        {
            long[] ent = entrada.Split(' ').Select(long.Parse).ToArray();
            Console.WriteLine(ent[0] ^ ent[1]);
            // XOR de dois valores
        }
    }
}