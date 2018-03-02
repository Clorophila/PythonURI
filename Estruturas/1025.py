def busca_binaria(lista,item):
    if lista[0]==item:
        return 0
    inicio = 0
    final = len(lista)-1
    while inicio < final:
        meio = (inicio+final)//2
        if lista[meio] == item:
            break
        elif lista[meio] > item:
            final = meio
        elif lista[meio] < item:
            inicio = meio+1
    if lista[-1]==item:
        meio == len(lista)-1
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