

def ajudandoGust_Avo(sequencia, subSeq):

    sol = [-1 for x in range(len(subSeq))]

    cont = 0

    for c in sequencia:

        if cont == (len(subSeq) - 1):

            if c == subSeq[cont]:

                if sol[len(subSeq) - 1] == -1:

                    sol[len(subSeq) - 1] = 1

                else:
                    sol[len(subSeq) - 1] += 1
        else:

            if c == subSeq[cont+1]:

                sol[cont+1] = 1
                cont += 1

            elif c == subSeq[cont]:

                if sol[cont] == -1:

                    sol[cont] = 1
                else:
                    sol[cont] += 1

    res = min(sol)

    if res == -1:
        return 0
    else:
        return res


if __name__ == '__main__':

    quant = int(input())

    for x in range(quant):

        seq1 = input()
        seq2 = input()

        res = ajudandoGust_Avo(seq1, seq2)

        print(res)
