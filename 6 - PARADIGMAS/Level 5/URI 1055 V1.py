from _collections import deque


def permutacaoElegante(permutacao):

    solucao = deque()
    solucao.append(permutacao.popleft())  # adiciona o menor elemento

    while permutacao:  # enquanto tiver elemento

        solucao.appendleft(permutacao.pop())  # adicione no inicio o maior elemento da lista

        if permutacao:
            solucao.append(permutacao.pop())  # adicione no fim o segundo maior maior elemento lista

        if permutacao:
            solucao.appendleft(permutacao.popleft())  # adicione no inicio o menor elemento da lista

        if permutacao:
            solucao.append(permutacao.popleft())  # adicione no fim o segundo menor maior elemento lista

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