
def verificaStringAdjacente(genoma):
    tam = len(genoma) // 2
    for x in range(1, tam + 1):
        prefixo = genoma[-x * 2:-x]
        radical = genoma[-x:]
        if prefixo == radical:
            return genoma[:-1]
    return genoma

def genomaIterativo(N):

    genoma = "N"
    trabalhoFeito = {"N": 1}

    ultimoGenoma = genoma[len(genoma) - 1]

    while len(genoma) < N:

        if ultimoGenoma == "N":

            genoma += "O"

            if genoma in trabalhoFeito:
                genoma = genoma[:-1] + "P"
                if genoma in trabalhoFeito:
                    genoma = genoma[:-2]
                    ultimoGenoma = genoma[len(genoma) - 1]
                else:
                    trabalhoFeito[genoma] = 1
                    genoma = verificaStringAdjacente(genoma)
                    ultimoGenoma = genoma[len(genoma) - 1]
            else:
                trabalhoFeito[genoma] = 1
                genoma = verificaStringAdjacente(genoma)
                ultimoGenoma = genoma[len(genoma) - 1]

        elif ultimoGenoma == "O":

            genoma += "N"

            if genoma in trabalhoFeito:
                genoma = genoma[:-1] + "P"

                if genoma in trabalhoFeito:
                    genoma = genoma[:-2]
                    ultimoGenoma = genoma[len(genoma) - 1]

                else:
                    trabalhoFeito[genoma] = 1
                    genoma = verificaStringAdjacente(genoma)
                    ultimoGenoma = genoma[len(genoma) - 1]
            else:

                trabalhoFeito[genoma] = 1
                genoma = verificaStringAdjacente(genoma)
                ultimoGenoma = genoma[len(genoma) - 1]

        elif ultimoGenoma == "P":

            genoma += "N"

            if genoma in trabalhoFeito:
                genoma = genoma[:-1] + "O"
                if genoma in trabalhoFeito:
                    genoma = genoma[:-2]
                    ultimoGenoma = genoma[len(genoma) - 1]
                else:
                    trabalhoFeito[genoma] = 1
                    genoma = verificaStringAdjacente(genoma)
                    ultimoGenoma = genoma[len(genoma) - 1]
            else:
                trabalhoFeito[genoma] = 1
                genoma = verificaStringAdjacente(genoma)
                ultimoGenoma = genoma[len(genoma) - 1]
    return genoma


if __name__ == "__main__":
    string = genomaIterativo(5000)

    entrada = int(input())

    while entrada != 0:
        print(string[:entrada])

        entrada = int(input())