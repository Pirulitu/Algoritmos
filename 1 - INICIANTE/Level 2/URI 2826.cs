using System;
using System.Collections;
using System.Linq;

class URI2826
{
    public static void Main(string[] args)
    {//poderia fazer um sort e dar a saida, mas nao teria proposito em resolver esse problema, assim irei fazer manualmente
        string str1 = Console.ReadLine();
        string str2 = Console.ReadLine();
        
        int max = Math.Min(str1.Length,str2.Length);//pega o tamanho da string de menor tamanho

        bool printa = false;
        // controla o estato se ao final vou imprimir as strings ou se ja foi empressa
        for (int i = 0; i < max; i++)
        {
            if (comparaChar(str1[i], str2[i]) == 0)//se a os caracteres na posicao i forem iguais passa para o proximo caracter
            {
                printa = true;
                continue;
            }
            
            if (comparaChar(str1[i], str2[i]) == 1)//se for 1 indica que a primeira string eh lexicamente menor que a segunda
            {
                Console.WriteLine(str1);
                Console.WriteLine(str2);
                printa = false;
                break;
            }
            // caso contrario indica que a segunda eh menor
            Console.WriteLine(str2);
            Console.WriteLine(str1);
            printa = false;
            break;
        }

        if (printa)        
        {
            if (max == str1.Length)
            {
                Console.WriteLine(str1);
                Console.WriteLine(str2);
            }
            else
            {
                Console.WriteLine(str2);
                Console.WriteLine(str1);
            }
        }
    }

    public static int comparaChar(char n1, char n2)
    {
        if (n1 < n2)
            return 1;
        if (n1 > n2)
            return 2;
        return 0;
            
    }
}