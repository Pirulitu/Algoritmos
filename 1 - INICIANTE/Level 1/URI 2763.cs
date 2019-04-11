using System; 
class URI2763 
{
        static void Main(string[] args)
        {
            
            string str = Console.ReadLine();
            //Metodo "SubString" com inicio e tamanho no argumento.
            string str1 = str.Substring(0, 3);
            string str2 = str.Substring(4, 3);
            string str3 = str.Substring(8, 3);
            string str4 = str.Substring(12, 2);
            Console.WriteLine(str1);
            Console.WriteLine(str2);
            Console.WriteLine(str3);
            Console.WriteLine(str4);
        }
}