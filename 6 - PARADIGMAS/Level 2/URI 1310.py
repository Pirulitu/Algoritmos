
def lucro(lucros):

    solucoes = [0]

    maxLucro = lucroPerdido = 0

    temPrimeiro = False

    for lucro in lucros:

        if not temPrimeiro:

            if lucro > 0:

                maxLucro = lucro
                solucoes.append(maxLucro)

                temPrimeiro = True
        else:

            if lucro < 0:
                lucroPerdido -= lucro

            else:

                if lucroPerdido > maxLucro:

                    maxLucro = lucro
                    solucoes.append(maxLucro)
                    lucroPerdido = 0

                else:
                    maxLucro += (lucro - lucroPerdido)
                    solucoes.append(maxLucro)
                    lucroPerdido = 0

    return max(solucoes)


if __name__ == '__main__':

    while True:

        try:
            quantDias = int(input())

            custoPorDia = int(input())

            lucrosDosDias = list()

            for _ in range(quantDias):

                lucroDia = int(input())

                lucrosDosDias.append(lucroDia-custoPorDia)

            maxLucro = lucro(lucrosDosDias)

            print(maxLucro)

        except EOFError:
            break
