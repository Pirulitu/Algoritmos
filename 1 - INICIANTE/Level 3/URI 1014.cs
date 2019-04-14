using System;

class URI1014
{
    public static void Main(string[] args)
    {
        
            int dist = Int32.Parse(Console.ReadLine());
            float comb = float.Parse(Console.ReadLine());
            float res = dist / comb;

            Console.WriteLine("{0:F3} km/l",res);

    }
}