using System; 

class URI1006 {
	
    static void Main(string[] args)
    {
        //ler tres valores e exibe a media com 5 cadas de precisao
        double a = double.Parse(Console.ReadLine());
        double b = double.Parse(Console.ReadLine());
        double c = double.Parse(Console.ReadLine());
        double x = ((a * 2) + (b * 3)+(c*5))/ 10;
        Console.WriteLine("MEDIA = {0:F1}", x);

    }

}