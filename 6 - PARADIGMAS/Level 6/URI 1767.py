def sacoPapaiNoel(conjuntos):

    brinquedos = 0

    sobra = len(conjuntos)

    capacidadeRestante = 50

    for razao, quantB, peso in conjuntos:

        if peso <= capacidadeRestante:

            capacidadeRestante -= peso

            brinquedos += quantB
            sobra -= 1

    pesototal = 50 - capacidadeRestante

    return brinquedos, pesototal, sobra


if __name__ == '__main__':

    testes = int(input())

    for _ in range(testes):

        conjuntosBrinquedos = int(input())

        conjuntos = list()

        for _ in range(conjuntosBrinquedos):
            quantB, pesoB = input().split()
            quantB, pesoB = int(quantB), int(pesoB)

            conjunto = (quantB / pesoB, quantB, pesoB)

            conjuntos.append(conjunto)

        conjuntos.sort(reverse=True)

        brinquedos, peso, sobra = sacoPapaiNoel(conjuntos)

        print(brinquedos, "brinquedos")
        print("Peso: %d kg" % peso)
        print("sobra(m) %d pacote(s)" % sobra)
