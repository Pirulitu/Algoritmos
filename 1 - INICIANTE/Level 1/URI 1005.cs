using System; 

class URI1005 {
	
    static void Main(string[] args)
    {
        //ler dois valores e exibe a media com 5 cadas de precisao
         double a = double.Parse(Console.ReadLine());
        double b = double.Parse(Console.ReadLine());
        double x = ((a * 3.5) + (b * 7.5)) / 11;
        Console.WriteLine("MEDIA = {0:F5}", x);

    }

}