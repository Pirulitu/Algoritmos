"""
Você tem que planejar o itinerário de modo que a distância máxima de um único salto seja minimizada? ir e voltar
"""
# passar como parametro a pedra que  eu to

def sapoDinamico(pedras, pedraAtual, solucao, boolIda, distMargem):
    if len(pedras) == 1:
        return max(solucao)

    else:

        atualPedraTipo = pedraAtual[0]
        atualPedraDist = int(pedraAtual[2:])

        proximaPedraTipo = pedras[1][0]
        proximaPedraDist = int(pedras[1][2:])

        salto = abs(atualPedraDist - proximaPedraDist)

        if atualPedraDist == distMargem:  # se  eu cheguei na margem set falso o valor de que eu estou na ida pra margem
            boolIda = False

        if proximaPedraTipo == 'S' and boolIda:

            s1 = sapoDinamico(pedras[1:], pedraAtual, solucao.copy(), boolIda, distMargem)

            removePedraPequena(pedras, pedras[1])

            solucao.append(salto)  # guarda o salto dado na solucao
            s2 = sapoDinamico(pedras[1:], pedras[1], solucao.copy(), boolIda, distMargem)

            return min(s1, s2)

        else:
            solucao.append(salto)
            return sapoDinamico(pedras[1:], pedras[1], solucao.copy(), boolIda, distMargem)

def removePedraPequena(pedras, elemento):

    aux = pedras.pop(1)

    pedras.remove(elemento)

    pedras.insert(1, aux)

    return pedras

def formataPedras(p, m):
    pedraMargemD = 'B-' + m
    pedraMargemE = 'B-0'

    p.insert(0, pedraMargemE)  # adiciona a margem esquerda
    p.append(pedraMargemD)  # adiciona a margem direita

    aux = p.copy()
    aux.pop()
    aux.reverse()

    p += aux

    return p


if __name__ == '__main__':

    casos = int(input())

    for x in range(casos):

        distMargem = input().split()[1]

        pedras = input().split()  # B big, S small, Int N

        pedras = formataPedras(pedras, distMargem)

        s = sapoDinamico(pedras, pedras[0], [], True, int(distMargem))

        print("Case %d: %d" % (x + 1, s))
