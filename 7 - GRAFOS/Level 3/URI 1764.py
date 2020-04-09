
def criaMapa(cidades):
    mapa = {}
    for v in range(cidades):  # cada vertice tem uma lista de vizinhos, inicialmente nao tem nenhum
        mapa[v] = {}
    return mapa


def adicionaAresta(CCD):

    cidade1 = int(CCD[0])
    cidade2 = int(CCD[1])
    distancia = int(CCD[2])

    if cidade1 in mapa[cidade2].keys():  # se a aresta ja existir, comparar e botar somente a menor

        if mapa[cidade2][cidade1] > distancia:  # se o valor atual for mair, substitui

            mapa[cidade2][cidade1] = distancia
            mapa[cidade1][cidade2] = distancia
    else:
        mapa[cidade2][cidade1] = distancia
        mapa[cidade1][cidade2] = distancia


def itinerarioDoPapaiNoel(cidades: dict):

    soma = 0
    alcancaveis = [0]
    naoAlcancaveis = [x for x in range(1, len(cidades))]

    naoAlcancouRestante = False

    while naoAlcancaveis:

        if naoAlcancouRestante:
            return soma

        for cidade in alcancaveis:  # pega a menor distancia que chega em minm
            pass


if __name__ == '__main__':

    entrada = input()

    while entrada != "0 0":

        entrada = entrada.split()
        cidades, caminhos = int(entrada[0]), int(entrada[1])

        mapa = criaMapa(cidades)

        for x in range(caminhos):

            CCD = input().split()
            adicionaAresta(CCD)

        res = itinerarioDoPapaiNoel(mapa)

        print(res)

        entrada = input()