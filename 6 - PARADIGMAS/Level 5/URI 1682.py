def verificaStringAdjacente(genoma):
    tam = len(genoma) // 2
    for x in range(2, tam + 1):
        prefixo = genoma[-x * 2:-x]
        radical = genoma[-x:]

        if prefixo == radical:
            return False
    return True


# salvar a que deu errado e comparar antes de calcular

def genoma():
    sequencia = "NONPNOPNPONOPNONPNOPNPONPNON"
    deuErrado = set()

    while len(sequencia) < 5001:

        ultimoGenoma = sequencia[-1]

        if ultimoGenoma == "N":

            sequencia += "O"

            if sequencia in deuErrado:

                sequencia = sequencia[:-1] + "P"

                if sequencia in deuErrado:

                    sequencia = sequencia[:-1]  # remove o P
                    deuErrado.add(sequencia)  # adiciona cadeia que nao deu certo nem com O nem com P ao dicionario
                    sequencia = sequencia[:-1]  # remove o N pra na proxima vez ele verificar e botar o P ou O

                else:
                    semConflito = verificaStringAdjacente(sequencia)

                    if semConflito:
                        continue

                    else:
                        deuErrado.add(sequencia)
                        sequencia = sequencia[:-1]
            else:
                semConflito = verificaStringAdjacente(sequencia)

                if semConflito:
                    continue

                else:
                    deuErrado.add(sequencia)
                    sequencia = sequencia[:-1]

        elif ultimoGenoma == "O":

            sequencia += "N"

            if sequencia in deuErrado:

                sequencia = sequencia[:-1] + "P"

                if sequencia in deuErrado:

                    sequencia = sequencia[:-1]  # remove o P
                    deuErrado.add(sequencia)  # adiciona cadeia que nao deu certo nem com O nem com P ao dicionario
                    sequencia = sequencia[:-1]  # remove o N pra na proxima vez ele verificar e botar o P ou O

                else:
                    semConflito = verificaStringAdjacente(sequencia)

                    if semConflito:
                        continue

                    else:
                        deuErrado.add(sequencia)
                        sequencia = sequencia[:-1]
            else:
                semConflito = verificaStringAdjacente(sequencia)

                if semConflito:
                    continue

                else:
                    deuErrado.add(sequencia)
                    sequencia = sequencia[:-1]

        elif ultimoGenoma == "P":

            sequencia += "N"

            if sequencia in deuErrado:

                sequencia = sequencia[:-1] + "O"

                if sequencia in deuErrado:

                    sequencia = sequencia[:-1]  # remove o P
                    deuErrado.add(sequencia)  # adiciona cadeia que nao deu certo nem com O nem com P ao dicionario
                    sequencia = sequencia[:-1]  # remove o N pra na proxima vez ele verificar e botar o P ou O

                else:
                    semConflito = verificaStringAdjacente(sequencia)

                    if semConflito:
                        continue

                    else:
                        deuErrado.add(sequencia)
                        sequencia = sequencia[:-1]
            else:
                semConflito = verificaStringAdjacente(sequencia)

                if semConflito:
                    continue

                else:
                    deuErrado.add(sequencia)
                    sequencia = sequencia[:-1]

    return sequencia

import time

if __name__ == "__main__":

    i = time.time()
    genoma = genoma()
    f = time.time()
    print(f - i)
    entrada = int(input())

    while entrada != 0:

        print(genoma[:entrada])

        entrada = int(input())
