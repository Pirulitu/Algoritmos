

def removeDuplicado(grafo, inicio, vizinho):  # remove arestas duplicadas
    while grafo[inicio].count((vizinho, 1)) > 1:
        grafo[inicio].remove((vizinho, 1))
    while (inicio, 1) in grafo[vizinho]:
        grafo[vizinho].remove((inicio, 1))
    return grafo


def criaGrafo(quant_v):  # cria um grafo (floresta) sem vertices, somente arestas

    grafo = list()
    for _ in range(quant_v):
        grafo.append(list())
    return grafo


def lerGrafo(v, a, grafo):  # le o grafo e adiciona as arestas
    for _ in range(a):
        v1, v2 = input().split()
        v1 = int(v1)
        v2 = int(v2)
        grafo[v1].append((v2, 1))
        grafo[v2].append((v1, 1))
    return grafo


def passeio(grafo, inicio):  # percorre o grafo contando quantos movimentos foram efetuados(visinhos alcançaveis)
    global count
    for aresta in grafo[inicio]:
        count += 1
        verticeVizinho = aresta[0]
        removeDuplicado(grafo, inicio, verticeVizinho)
        passeio(grafo, verticeVizinho)
        count += 1
    return count


if __name__ == "__main__":

    quant_teste = int(input())
    for x in range(quant_teste):
        count = 0
        vertice_inicial = int(input())

        quantVertices, quantArestas = input().split()

        quantVertices = int(quantVertices)
        quantArestas = int(quantArestas)

        grafo = criaGrafo(quantVertices)
        lerGrafo(quantVertices, quantArestas, grafo)
        print(passeio(grafo, vertice_inicial))
