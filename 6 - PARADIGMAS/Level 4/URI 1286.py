def motoboy(pedidos, quantTotal):

    entregas = []

    for x in range(len(pedidos) + 1):
        entregas.append([0 for x in range(quantTotal + 1)])

    for pedido in range(1, len(pedidos) + 1):

        for ca in range(1, quantTotal + 1):

            pedidoAtual = pedido - 1
            tempoEntrega = pedidos[pedidoAtual][0]
            quantPizza = pedidos[pedidoAtual][1]

            if quantPizza <= ca:

                if tempoEntrega + entregas[pedidoAtual][ca - quantPizza] > entregas[pedidoAtual][ca]:
                    entregas[pedido][ca] = tempoEntrega + entregas[pedidoAtual][ca - quantPizza]

                else:
                    entregas[pedido][ca] = entregas[pedidoAtual][ca]

            else:
                entregas[pedido][ca] = entregas[pedidoAtual][ca]

    tempo = entregas[len(pedidos)][quantTotal]

    return tempo


if __name__ == '__main__':

    quantPedidos = int(input())

    while quantPedidos != 0:

        tempoEntrega = int(input())

        pedidos = []

        for x in range(quantPedidos):
            p = input().split()
            p = (int(p[0]), int(p[1]))
            pedidos.append(p)

        pedidos.sort(reverse=True)

        res = motoboy(pedidos, tempoEntrega)

        print(res, "min.")

        quantPedidos = int(input())
