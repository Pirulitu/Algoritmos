using System; 
using System.Linq;
class URI1589
{
        static void Main(string[] args)
        { 
            //Fazer um circulo de raio c onde cabe dois circulos de raios diferestes ou igual
            int n = Int32.Parse(Console.ReadLine());
            for (int i = 0; i < n; i++)
            {
                string s = Console.ReadLine();
                int[] parNumero = s.Split(' ').Select(Int32.Parse).ToArray();
                //obs: o compilador pdoe dar erro em algumas versões se utilizar aspals duplas no split
                int c = parNumero[0] + parNumero[1];
                Console.WriteLine(c);

            }
        }
}