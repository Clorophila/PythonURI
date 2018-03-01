case = 0
while True:
    case += 1

    n, q = map(int,input().split())

    if(n==0 and q==0):
        break

    marmores = []
    consultas = []
    k = 0

    for marmore in range(n):
        valor = int(input())
        flag = False
        for i in range(k):
            if valor<=marmores[i]:
                marmores.insert(i,valor)
                flag = True
                break
        if not flag:
            marmores.append(valor)
        k+=1

    for consulta in range(q):
        consultas.append(int(input()))

    print('CASE# {}:'.format(case))

    for consulta in range(q):
        valor = consultas[consulta]
        flag = False
        for i in range(n):
            if valor==marmores[i]:
                print('{} found at {}'.format(valor,i+1))
                flag = True
                break
        if not flag:
            print('{} not found'.format(valor))