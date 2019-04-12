using System;
using System.Linq;
class URI2168
{
        static void Main(string[] args)
        {
            string input;
            int n = Int32.Parse(Console.ReadLine());
            short[,] matrizQuadras = new short[n+1,n+1];
            for (int i = 0; i <= n; i++)
            {
                input = Console.ReadLine();
                short[] linha = input.Split(' ').Select(short.Parse).ToArray();
                //leitura de linha da matriz e conversao para array de short int
                for (int j = 0; j <= n; j++)
                {
                    matrizQuadras[i,j] = linha[j];
                    //adiciona o array lido na matriz
                }
               
            }
            
            short quadra1, quadra2, quadra3, quadra4;
            //quadra com 4 esquinas
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < n; j++)
                {
                    //para cada quadra pegue os valores da matriz
                    quadra1 = matrizQuadras[i,j];
                    quadra2 = matrizQuadras[i,j+1];
                    quadra3 = matrizQuadras[i+1,j];
                    quadra4 = matrizQuadras[i+1,j+1];
                    if (quadra1+quadra2+quadra3+quadra4 > 1)
                    //se tiver mais de 2 ou mais cameras esta seguro, se nao nao esta
                        Console.Write("S");
                    else
                        Console.Write("U");
                }

                Console.WriteLine();
            }

        }
}