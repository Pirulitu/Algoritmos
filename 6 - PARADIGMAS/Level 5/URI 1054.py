"""
Você tem que planejar o itinerário de modo que a distância máxima de um único salto seja minimizada? ir e voltar
"""


# passar como parametro a pedra que  eu to

def sapoDinamico(pedras):

    vezI = True  # inicialmente a proxima pedra pequena o sapo da ida pode pular
    solucao = []

    sapoI = int(pedras[0][2:])  # sapo da ida inicia em 0
    sapoV = int(pedras[0][2:])  # sapo da volta tb pq ele vai fazer o percurso da volta, so que inverso

    for x in range(1, len(pedras)):

        pedraAtualDist = int(pedras[x][2:])
        pedraAtualTipo = pedras[x][0]

        if pedraAtualTipo == 'S':  # se a pedra for pequena, so um sapo pode usar

            if vezI:  # se for a vez do sapo da ida

                saltoI = abs(pedraAtualDist - sapoI)  # tamanho do pulo que o sapo da ida vai dar
                sapoI = pedraAtualDist  # o sapo deu o pulo e ficou na pedra
                solucao.append(saltoI)  # o salto é contado na solucao

                vezI = False  # proxima vez é so sapo da Volta

            else:  # vez do sapo da volta
                saltoJ = abs(pedraAtualDist - sapoV)
                sapoV = pedraAtualDist
                solucao.append(saltoJ)

                vezI = True  # proxima vez é so sapo da Ida

        else:  # se for grande, os dois sapos pulam pra ela
            saltoI = abs(pedraAtualDist - sapoI)
            saltoJ = abs(pedraAtualDist - sapoV)
            sapoI = pedraAtualDist
            sapoV = pedraAtualDist
            solucao.append(saltoI)
            solucao.append(saltoJ)

    return max(solucao)

def formataPedras(p, m):

    pedraMargemD = 'B-' + m
    pedraMargemE = 'B-0'

    p.insert(0, pedraMargemE)  # adiciona a margem esquerda
    p.append(pedraMargemD)  # adiciona a margem direita

    return p


if __name__ == '__main__':

    casos = int(input())

    for x in range(casos):
        distMargem = input().split()[1]

        pedras = input().split()  # B big, S small, Int N

        pedras = formataPedras(pedras, distMargem)

        s = sapoDinamico(pedras)

        print("Case %d: %d" % (x + 1, s))
