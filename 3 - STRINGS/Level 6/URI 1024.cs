using System;
using System.Linq;
using System.Text;

class URI1024
{
        static void Main(string[] args)
        {   
            int n = Int32.Parse(Console.ReadLine());
            for (int k = 0; k < n; k++)
            {
                string inp = Console.ReadLine();
                char[] str = inp.ToCharArray();
                //string  é imutavel e assim convertemos para vetor de char
                for (int i = 0; i < str.Length; i++)
                    if (char.IsLetter(str[i]))// se for letra
                        str[i] = Convert.ToChar(Convert.ToInt32(str[i]) + 3);
                        //converto a posição da letra para o numero da tabela, 
                        //avanço 3 casas na tabela e converto o novo valor da tabela 
                        //pra seu respectivo caracter
                Array.Reverse(str);
                // inverto o array
                int meio = (int)Math.Truncate((float)(str.Length / 2));
                // meio do array piso
                for (int i = meio; i < str.Length; i++)
                    str[i] = Convert.ToChar(Convert.ToInt32(str[i]) - 1);
                    // desloco todos caracteres para o caracter anterior na tabela
                Console.WriteLine(str);
            }
            
        }
}