using System; 
using System.Linq;
class URI1858 {

    static void Main(string[] args)
    { 
        //imprimir o menor valor de um vetor 
        int n = Int32.Parse(Console.ReadLine());
        string input = Console.ReadLine();
        int[] pessoas = input.Split(' ').Select(Int32.Parse).ToArray();
        int indexMin = 0;
        for (int i = 0; i < pessoas.Length; i++)
            if (pessoas[indexMin] > pessoas[i])
                indexMin = i;

        Console.WriteLine(indexMin+1);
    }

}