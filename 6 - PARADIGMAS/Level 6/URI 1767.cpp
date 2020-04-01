#include <iostream>
#include <string>
#include <tuple>

using namespace std;

int main()
{
  std::string name;
  std::cout << "What is your name? ";
  getline (std::cin, name);
  std::cout << "Hello, " << name << "!\n";
}






def sacoPapaiNoel(conjuntos, sobra, capRestante=50, brinquedos=0):

    if len(conjuntos) == 1:

        if conjuntos[0][1] <= capRestante:
            return brinquedos + conjuntos[0][0], 50 - (capRestante - conjuntos[0][1]), sobra - 1
        else:
            return brinquedos, 50 - capRestante, sobra

    else:

        quantB = conjuntos[0][0]
        pesoB = conjuntos[0][1]

        if pesoB <= capRestante:

            brinquedos1, peso1, sobra1 = sacoPapaiNoel(conjuntos[1:], sobra-1, capRestante-pesoB, brinquedos+quantB)
            brinquedos2, peso2, sobra2 = sacoPapaiNoel(conjuntos[1:], sobra, capRestante, brinquedos)

            if brinquedos1 > brinquedos2:
                return brinquedos1, peso1, sobra1
            else:
                return brinquedos2, peso2, sobra2

        else:
            brinquedos2, peso2, sobra2 = sacoPapaiNoel(conjuntos[1:], sobra, capRestante, brinquedos)
            return brinquedos2, peso2, sobra2


if __name__ == '__main__':

    testes = int(input())

    for _ in range(testes):

        conjuntosBrinquedos = int(input())

        conjuntos = list()

        for _ in range(conjuntosBrinquedos):
            quantB, pesoB = input().split()
            quantB, pesoB = int(quantB), int(pesoB)

            conjunto = (quantB, pesoB)

            conjuntos.append(conjunto)

        brinquedos, peso, sobra = sacoPapaiNoel(conjuntos, len(conjuntos))

        print(brinquedos, "brinquedos")
        print("Peso: %d kg" % peso)
        print("sobra(m) %d pacote(s)" % sobra)
