def caixeiroNoMuseu(grafo, temposVisita, naoVisitados, mAnterior, minRestante=420, qMuseu=0):

    if minRestante == 0:
        return 0

    elif len(naoVisitados) == 1:
        tempoTour = temposVisita[naoVisitados[0]]
        tempoDeslocamento = mAnterior[naoVisitados[0]]
        if minRestante >= tempoTour + tempoDeslocamento:
            return 1
        else:
            return 0

    else:
        s1 = s2 = 0

        for museu in range(len(grafo)):

            if museu in naoVisitados:
                continue

            tempoTour = temposVisita[museu]

            if tempoTour + mAnterior[museu] <= minRestante:
                s1 = max(s1, caixeiroNoMuseu(grafo, temposVisita, naoVisitados + [museu], grafo[museu],
                                             minRestante - tempoTour - mAnterior[museu], qMuseu + 1))
                s2 = max(s2, caixeiroNoMuseu(grafo, temposVisita, naoVisitados + [museu], mAnterior, minRestante, qMuseu))
            else:
                s2 = max(s2, caixeiroNoMuseu(grafo, temposVisita, naoVisitados + [museu], mAnterior, minRestante, qMuseu))

    return max(s1, s2)


if __name__ == '__main__':

    museus = int(input())

    while museus != 0:

        grafo = []

        temposVisita = input().split()
        temposVisita = [int(x) for x in temposVisita]

        for v in range(museus):
            vizinhos = input().split()
            vizinhos = [int(x) for x in vizinhos]

            grafo.append(vizinhos)

        museuAnterior = [0 for x in range(len(grafo))]
        s = caixeiroNoMuseu(grafo, temposVisita, [], museuAnterior)

        print(s)
        museus = int(input())
