def cortandoCanosPD(canos: list, compDisponivel: int):

    canosSol = [0 for x in range(compDisponivel + 1)]  # vetor com D1 para memorizar a soluçao

    for c in range(compDisponivel + 1):  # simula a matriz de itens X ComprimentoDisponivel

        for cr in range(len(canos)):

            canoAtual = cr
            canoComp = canos[canoAtual][0]
            canoValor = canos[canoAtual][1]

            if canoComp <= c:  # se o item atual couber na solucao, pegue o max entre a solucao anterior essa solucao

                canosSol[c] = max(canosSol[c], canosSol[c - canoComp] + canoValor)

    total = canosSol[compDisponivel]
    return total


if __name__ == '__main__':

    canosN, compDisp = input().split()
    canosN, compDisp = int(canosN), int(compDisp)

    canos = list()

    for _ in range(canosN):
        canoC, canoV = input().split()

        cano = (int(canoC), int(canoV))
        canos.append(cano)

    totalValor = cortandoCanosPD(canos, compDisp)

    print(totalValor)
