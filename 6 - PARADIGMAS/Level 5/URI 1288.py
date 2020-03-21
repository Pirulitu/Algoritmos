def carregarCanhaoBT(projeteis: object, capacidadeCanhao: int, danoProjeteis: int = 0):
    if not projeteis or capacidadeCanhao == 0:
        return danoProjeteis

    else:
        if capacidadeCanhao > 0:  # se ainda for possivel por mais peso no canhao

            danoProjetil, pesoProjetil = projeteis[0][0], projeteis[0][1]

            if capacidadeCanhao >= pesoProjetil:  # se o peso restante do canhao suportar o peso do projetil atual

                s1 = carregarCanhaoBT(projeteis[1:], capacidadeCanhao - pesoProjetil, danoProjeteis + danoProjetil)
                s2 = carregarCanhaoBT(projeteis[1:], capacidadeCanhao, danoProjeteis)

                return max(s1, s2)
            else:
                return carregarCanhaoBT(projeteis[1:], capacidadeCanhao, danoProjeteis)
        else:

            return danoProjeteis


def carregarCanhaoPD(projeteis: list, capacidadeCanhao: int):
    canhao = []
    # inicializa uma matriz preenchida com 0 (nao tem escolhas feitas)pra memorizar os itens que ja foram escolhidos.
    for x in range(len(projeteis) + 1):
        canhao.append([0 for x in range(capacidadeCanhao + 1)])

    for proj in range(len(projeteis) + 1):

        for cc in range(capacidadeCanhao + 1):

            projAtual = proj - 1
            danoProjAtual = projeteis[projAtual][0]
            pesoProjAtual = projeteis[projAtual][1]

            if proj == 0 or cc == 0:  # se o projetil
                canhao[proj][cc] = 0

            elif projeteis[projAtual][1] <= cc:  # se o peso do projetil for menor do que a capacidade do canhao
                #  guarde na solucao atual o valor maximo pegando ou nao pegando o projetil, ou seja
                #  entre o valor da solucao com o projetil e o valor da solucao sem ele
                #  a capacidade é subtraida (cc - pesoProjAtual)
                canhao[proj][cc] = max(danoProjAtual + canhao[projAtual][cc - pesoProjAtual], canhao[projAtual][cc])
            else:  # caso contrario, guarde na solucao atual o valor da solucao anterior
                canhao[proj][cc] = canhao[projAtual][cc]

    # a posicao da linha e da coluna da matriz(solucao) que tem maior soma de ()
    danoProjeteis = canhao[len(projeteis)][capacidadeCanhao]
    return danoProjeteis


if __name__ == '__main__':

    casos = int(input())

    for _ in range(casos):

        projeteis = list()
        projeteisQ = int(input())

        for _ in range(projeteisQ):
            poderDestruicao, peso = input().split()

            projetil = (int(poderDestruicao), int(peso))
            projeteis.append(projetil)

        capacidadeCanhao = int(input())  # capacidade do canhão em peso
        resistenciaCastelo = int(input())  # resistencia do castelo em dano

        dano = carregarCanhaoPD(projeteis, capacidadeCanhao)

        if dano >= resistenciaCastelo:
            print("Missao completada com sucesso")
        else:
            print("Falha na missao")
