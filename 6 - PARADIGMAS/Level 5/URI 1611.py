def elevadorLotado(paradas, capacidade):

    energiaGasta = 0

    while paradas:

        ultimo = paradas[-1]

        energiaGasta += 2*ultimo

        paradas = paradas[:-capacidade]

    return energiaGasta


if __name__ == '__main__':

    testes = int(input())

    for x in range(testes):
        NCM = input().split()

        capacidade = int(NCM[1])

        destinhos = input().split()

        destinhos = [int(x) for x in destinhos]

        destinhos.sort()

        s = elevadorLotado(destinhos, capacidade)

        print(s)
