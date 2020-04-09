
""""
14 4 20
14 palavras tem o texto
4 linhas por pagina
20 caracteres por linha
Se mana Piedade tem casado com Quincas Borba apenas me daria uma esperanca colateral
"""


def concursoDeContos(conto, maxLinhas, maxCaraxteres):

    paginas = 0

    if len(conto) > 0:
        paginas = 1

    caracteresRestantes = maxCaracteres
    linhasRestantes = maxLinhas - 1

    for palavra in conto:

        if len(palavra) <= caracteresRestantes:

            caracteresRestantes -= len(palavra) + 1

        else:

            if linhasRestantes == 0:

                paginas += 1

                caracteresRestantes = maxCaracteres - (len(palavra) + 1)
                linhasRestantes = maxLinhas - 1

            else:
                linhasRestantes -= 1
                caracteresRestantes = maxCaracteres - (len(palavra) + 1)

    return paginas


if __name__ == '__main__':

    while True:
        try:
            entrada = input().split()

            conto = input().split()

            maxLinhasPorPagina = int(entrada[1])
            maxCaracteres = int(entrada[2])

            pgs = concursoDeContos(conto, maxLinhasPorPagina, maxCaracteres)
            print(pgs)
        except EOFError:
            break

