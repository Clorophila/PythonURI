import itertools
while True:
    try:
        entrada = input()
        sequencias = set()

        for i in range(1,len(entrada)+1):
            aux = list(itertools.permutations(entrada,i))
            for item in aux:
                sequencias.add(''.join(item))
        resultado = sorted(list(sequencias))
        print(resultado)
        for item in resultado:
            print(item)
        print()

    except EOFError:
        break