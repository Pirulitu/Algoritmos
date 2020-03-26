from _collections import deque

def permutacaoElegante(permutacao):

    if len(permutacao) <= 1:
        return 0

    impar = False

    if len(permutacao) % 2 == 1:
        elementoMeio = permutacao[len(permutacao)//2]
        impar = True

    solucao = deque()

    for x in range(len(permutacao)//2):  # enquanto tiver elemento

        if x % 2 == 0:
            solucao.appendleft(permutacao.popleft())
            solucao.append(permutacao.pop())

        else:
            solucao.appendleft(permutacao.pop())
            solucao.append(permutacao.popleft())

    if impar:
        if abs(solucao[0] - elementoMeio) > abs(solucao[-1] - elementoMeio):
            solucao.appendleft(elementoMeio)

        else:  # se nao adicione no final
            solucao.append(elementoMeio)

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
        entrada = input().split()
        quant = int(entrada[0])
        permutacao = entrada[1:quant+1]
        permutacao = formata(permutacao)
        sol = permutacaoElegante(permutacao)
        print("Case %d: %d" % (x + 1, sol))
