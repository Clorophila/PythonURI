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
            print('{} found at {}'.format(valor,marmores.index(valor)+1))
        except:
            print('{} not found'.format(valor))