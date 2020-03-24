from _collections import deque


def permutacaoElegante(permutacao):

    solucao = deque()
    solucao.append(permutacao.popleft())  # adiciona o menor elemento

    while permutacao:  # enquanto tiver elemento

        # se a diferenca do primeiro elemento da solucao com o maior elemento da permutacao(atual) for maior que
        # a diferenca do ultimo elemento da solucao com o maior elemento da permutacao(atual), adicione no inicio
        maiorElementoP = permutacao[-1]  # maior elemento da permutacao atual
        if abs(solucao[0] - maiorElementoP) > abs(solucao[-1] - maiorElementoP):
            solucao.appendleft(permutacao.pop())

        else:  # se nao adicione no final
            solucao.append(permutacao.pop())

        if permutacao:
            maiorElementoP = permutacao[-1]  # maior elemento da permutacao atual
            if abs(solucao[0] - maiorElementoP) > abs(solucao[-1] - maiorElementoP):
                solucao.appendleft(permutacao.pop())

            else:  # se nao adicione no final
                solucao.append(permutacao.pop())

        # se a diferenca do primeiro elemento da solucao com o menor elemento da permutacao(atual) for maior que
        # a diferenca do ultimo elemento da solucao com o menor elemento da permutacao(atual), adicione no inicio
        if permutacao:

            menorElementoP = permutacao[0]  # maior elemento da permutacao atual
            if abs(solucao[0] - menorElementoP) > abs(solucao[-1] - menorElementoP):

                solucao.appendleft(permutacao.popleft())

            else:
                solucao.append(permutacao.popleft())

        if permutacao:

            menorElementoP = permutacao[0]  # maior elemento da permutacao atual
            if abs(solucao[0] - menorElementoP) > abs(solucao[-1] - menorElementoP):

                solucao.appendleft(permutacao.popleft())

            else:
                solucao.append(permutacao.popleft())

    res = 0

    for x in range(len(solucao) - 1):  # calcula a somatória do valor absoluto da subtracao dos valores adjacentes
        res += abs(solucao[x] - solucao[x + 1])

    return res


def formata(perm):

    perm = [int(x) for x in perm]
    perm.sort()

    perm = deque(perm)
    return perm


if __name__ == '__main__':

    casos = int(input())

    for x in range(casos):

        permutacao = input().split()[1:]
        permutacao = formata(permutacao)
        sol = permutacaoElegante(permutacao)

        print("Case %d: %d" % (x + 1, sol))
