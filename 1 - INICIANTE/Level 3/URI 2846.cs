using System;
using System.Collections;
using System.Linq;
class URI2846
{
    public static void Main(string[] args)
    {    
        int n = Int32.Parse(Console.ReadLine());
        
        int[] fibList = fibonacci(1000000);
        //10^5 eh a quantidade de elementos da sequencia que se deseja
        int[] notfibList = notFibonacci(fibList,1000000);

        Console.WriteLine(notfibList[n-1]);
    }

    public static int[] notFibonacci(int[] fibList, int max)
    {
        // apesar da função a principio parecer quadratica, a condição de fazer ate o vetor ter max elementos, faz com que assintoticamente seja linear na entrada max.
        int[] notFibList = new int[max];

        int count = 0;
        int i = 0;

        while (count < max)//enquanto nao tiver a quantidade max de indices...
        {
            if (fibList[i + 1] - fibList[i] > 1)
            //se a diferença entre dois numeros fib em sequencia crescente for maior que 1
            //isso indica que existe pelo menos 1 elemento da sequencia notFibonacci
                for (int j = fibList[i] + 1; j < fibList[i+1]; j++)
                //para j do fib de i + 1 ate fib (i+1) - 1 faça
                {
                    if (count < max)//verificação para nao ultrapassar o limite do vetor
                    {
                        notFibList[count] = j;
                        count++;
                    }
                    else
                        break;
                }
            i++;
        }
        return notFibList;
    }
    public static int[] fibonacci(int max)
    {
        int[] fibList = new int[max];

        fibList[0] = 1;
        fibList[1] = 1;

        for (int i = 2; i < max; i++)
            fibList[i] = fibList[i - 1] + fibList[i - 2];

        return fibList;
    }

}
