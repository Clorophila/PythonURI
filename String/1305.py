import math
while True:
    try:
        valor = float(input())
        cutoff = float(input())

        inteiro = int(math.floor(valor))

        if (valor-inteiro) > cutoff:
            print(inteiro+1)
        else:
            print(inteiro)

    except EOFError:
        break