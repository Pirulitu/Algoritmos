using System; 
using System.Linq;
class URI2029
{
        static void Main(string[] args)
        { 
            //recebe volume e diametro para calcular a altura que o
            //cilindro deve ter pra caber o volume e retornar sua area tambem

            string input;// = Console.ReadLine();
            while (!string.IsNullOrEmpty(input = Console.ReadLine()))//input != null && input != ""
            {
                float volume = float.Parse(input);
                float diametro = float.Parse(Console.ReadLine());

                float pi = 3.14F;
                float raio = diametro / 2;
                float altura = volume / (pi * (float)Math.Pow(raio, 2));
                float area = pi * (float)Math.Pow(raio, 2);
                Console.WriteLine("ALTURA = {0:F2}", Math.Round(altura, 2, MidpointRounding.ToEven)); //Math.Truncate(altura*1000)/1000);
                Console.WriteLine("AREA = {0:F2}",Math.Round(area,2,MidpointRounding.ToEven));
                    //Math.Truncate(area*100)/100); truncate pega a parte inteira de um float
            }
        }
}