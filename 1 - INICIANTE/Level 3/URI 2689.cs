using System;
using System.Collections;
using System.Linq;

class URI2689
{
    public static void Main(string[] args)
    {    
        int n = Int32.Parse(Console.ReadLine());

        for (int i = 0; i < n; i++)
        {    
            Hashtable repeat = new Hashtable();
            string print = "";
            
            string entrada1 = Console.ReadLine();
            int[] line1 = entrada1.Split(' ').Select(Int32.Parse).ToArray();
            
            string entrada2 = Console.ReadLine();
            int[] line2 = entrada2.Split(' ').Select(Int32.Parse).ToArray();

            string entrada3 = Console.ReadLine();
            int[] line3 = entrada3.Split(' ').Select(Int32.Parse).ToArray();
            
            compara(line1, repeat);//a função compara pega os 3 valores da linha da matriz e faz o abs da diferenca 
            compara(line2, repeat);//com o valor da frente para o primeiro valor e para os demais o valor anterior a ele
            compara(line3, repeat);//guarda esse abs na tabela de key adiciona 1, se existir a key incrementa ela. 
            
            
            int most_repeated = mostRepeated(repeat);
            // percorre a tabela e verifica qual a chave que tem maior repetição, pega a primeira chave se existir mesma quantidade

            print += comparaWithMostRepeted(line1, most_repeated, "");//a função comparaWithMostRepeted pega a key de maior repeticao
            print += comparaWithMostRepeted(line2, most_repeated, ""); // e compara com o abs de cada valor com os demais da linha
            print += comparaWithMostRepeted(line3, most_repeated, "");// se esse abs for igual a key, nao exite, caso contrario, exite
            print = print.Substring(0,print.Length-2);
            print += ";";
            Console.WriteLine("Possiveis maletas: {0}",print);
        }
    }

    public static Hashtable compara(int[] lista, Hashtable repeat)
    {
        int n1 = lista[0], n2 = lista[1], n3 = lista[2];
        int abs_n1 = Math.Abs(n1 - n2);
        int abs_n2 = Math.Abs(n2 - n1);
        int abs_n3 = Math.Abs(n3 - n2);

        if (repeat.Contains(abs_n1))
            repeat[abs_n1] = (int)repeat[abs_n1]+1;
        else
            repeat.Add(abs_n1,1);  
        
        if (repeat.Contains(abs_n2))
            repeat[abs_n2] = (int)repeat[abs_n2]+1;
        else
            repeat.Add(abs_n2,1);  
        
        if (repeat.Contains(abs_n3))
            repeat[abs_n3] = (int)repeat[abs_n3]+1;
        else
            repeat.Add(abs_n3,1);  
        
        return repeat;
    }

    public static int mostRepeated(Hashtable repeat)
    {
        int most_repeated = 0, value_most_repeated = -1;

        foreach (var key in repeat.Keys)
        {
            if((int)repeat[key] > value_most_repeated)
            {
                most_repeated = (int)key;
                value_most_repeated = (int)repeat[key];
            }
        }
        
        return most_repeated;
    }
    public static string comparaWithMostRepeted(int[] lista, int most_repeated,String print)
    {
        int n1 = lista[0], n2 = lista[1], n3 = lista[2];
        
        int n12 = Math.Abs(n1 - n2);
        int n13 = Math.Abs(n1 - n3);
        int n23 = Math.Abs(n2 - n3);

        if (n12 != most_repeated && n13 != most_repeated)
            print += n1.ToString() + ", ";
                    
        if (n12 != most_repeated && n23 != most_repeated)
            print += n2.ToString() + ", ";
        
        if (n13 != most_repeated && n23 != most_repeated)
            print += n3.ToString() + ", ";
        return print;
    }
}