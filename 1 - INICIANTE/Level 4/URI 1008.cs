using System;
class URI1008
{
        static void Main(string[] args)
        {
            //calcular o salario do funcionario baseado 
            //nas horas feitas e quanto ganha por hora
            int number = Int32.Parse(Console.ReadLine());
            int  horas = Int32.Parse(Console.ReadLine());
            float rsHora = float.Parse(Console.ReadLine());
            Console.WriteLine("NUMBER = {0}",number);
            Console.WriteLine("SALARY = U$ {0:F2}",rsHora*horas);
        }
}