def busca_binaria(lista,item):
    inicio = 0
    final = len(lista)

    while inicio < final:
        meio = (inicio+final)//2
        if lista[meio] == item:
            break
        elif lista[meio] > item:
            final = meio - 1
        elif lista[meio] < item:
            inicio = meio + 1
    if lista[meio] == item:
        while lista[meio] == item:
            meio -= 1
        return meio+1
    else:
        raise ValueError

case = 0
while True:
    n, q = map(int,input().split())

    if(n==0 and q==0):
        break

    case += 1
    marmores = []
    consultas = []

    for marmore in range(n):
        marmores.append(int(input()))
    for consulta in range(q):
        consultas.append(int(input()))

    marmores.sort()

    print('CASE# {}:'.format(case))

    for consulta in range(q):
        valor = consultas[consulta]
        try:
            print('{} found at {}'.format(valor,busca_binaria(marmores,valor)+1))
        except:
            print('{} not found'.format(valor))