import math


def calculaBase(n):
    # formula do tringulo da com base N que tem nElementos = n(n+1)/2 entao ao resolver a equaçao do segundo grau
    # com a = c = 1 nos da o numero da base na raiz positiva (x1)

    a = b = 1
    c = -(2 * n)

    x1 = (-1 + math.floor(math.sqrt(1 + (-4 * c)))) // 2

    return x1


def AVoltaParaCasa(pecas, orcamento):
    quantVolume = 0

    for razao, volume, preco in pecas:

        if preco <= orcamento:

            quantVolume += volume
            orcamento -= preco

        else:

            quantVolume += (volume / preco) * orcamento

            orcamento -= orcamento

            break

    return quantVolume


def ignoraDivisao0(volume, preco):
    return preco / volume


if __name__ == '__main__':

    orcamento = int(input().split()[1])

    pecasVolume = input().split()
    pecasVolume = [int(x) for x in pecasVolume]

    pecasPrecos = input().split()
    pecasPrecos = [int(x) for x in pecasPrecos]

    pecas = []

    for i in range(len(pecasVolume)):
        r = ignoraDivisao0(pecasVolume[i], pecasPrecos[i])

        peca = (r, pecasVolume[i], pecasPrecos[i])

        pecas.append(peca)

    pecas.sort()

    quantPecas = AVoltaParaCasa(pecas, orcamento)

    print(calculaBase(quantPecas))
