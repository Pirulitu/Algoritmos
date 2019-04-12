using System;
using System.Linq;

class URi1047
{
    static void Main(string[] args)
    {
            string input = Console.ReadLine();
            int[] numbers = input.Split(' ').Select(Int32.Parse).ToArray();
            int horaInicio = numbers[0];
            int horaFim = numbers[2];
            int minInicio = numbers[1];
            int minFim = numbers[3];
            int hora, min;
            if (horaInicio < horaFim)
                hora = horaFim - horaInicio;
            else
                 hora = 24 - (horaInicio - horaFim);

            min = minFim - minInicio;

            if (min < 0)
            {
                min = 60 + min;
                hora -= 1;
            }

            Console.WriteLine("O JOGO DUROU {0} HORA(S) E {1} MINUTO(S)",hora,min);

    }
}