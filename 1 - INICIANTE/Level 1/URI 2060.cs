using System; 
using System.Linq;
class URI2060 
{
        static void Main(string[] args)
        {
            int n = Int32.Parse(Console.ReadLine());
            string str = Console.ReadLine();
            //var array = str.Split(' ').Select(Int32.Parse).ToList(); conversao de string para lista de elementos
            int[] numbers = str.Split(' ').Select(Int32.Parse).ToArray();//conversao para vetor de elementos
            int count2, count3, count4, count5;
            count2 = count3 = count4 = count5 = 0;
            foreach (int number in numbers)
            {
                if (number % 2 == 0)
                    count2++;
                if (number % 3 == 0)
                    count3++;
                if (number % 4 == 0)
                    count4++;
                if (number % 5 == 0)
                    count5++;
            }

            Console.WriteLine("{0} Multiplo(s) de 2\n" +
                              "{1} Multiplo(s) de 3\n" +
                              "{2} Multiplo(s) de 4\n" +
                              "{3} Multiplo(s) de 5", count2, count3, count4, count5);
        }
}