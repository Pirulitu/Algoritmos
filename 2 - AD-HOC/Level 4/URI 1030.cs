using System;
using System.Collections;
using System.Linq;
using System.Text;

class URI1030
{
    public static void Main(string[] args)
    {
        int n = Int32.Parse(Console.ReadLine());//quantidade de testes
        for (int i = 0; i < n; i++)
        {
            var entrada = Console.ReadLine();// leitura de cada entrada de teste
            
            int[] par = entrada.Split(' ').Select(Int32.Parse).ToArray();
            //converte a entrada dada em string para vetor inteiro
            
            int len = par[0], salto = par[1];//start das variaveis len e salto correspondentes a entrada
            
            ArrayList vec = new ArrayList();//cria ArrayList
            
            for (int j = 0; j < len; j++)//cria um array de tamanho 'len' e inicia cada posição de 1 ate len
                vec.Add(j+1);

            int count = -1, passos = 0;
            
            while (vec.Count > 1)//enquanto tiver mais de 1 elemento
            {
                count += 1;
                passos += 1;
                if (count % vec.Count == 0)//se o contador passar do tamanho do Array em 1 posicao, set 0 (posição inicial do Array)
                    count = 0;
                if (passos==salto)
                // se a quantidade de passos for a definida pra o salto,
                // remova o elemento, reset os passos e o contador vai pra posicao anterior 
                {
                    passos = 0;
                    vec.RemoveAt(count);
                    count -= 1;
                }
            }
            Console.WriteLine("Case {0}: {1}",i+1,vec[0]);
        }
    }
}