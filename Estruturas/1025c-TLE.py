def quicksort(data):
    if len(data) < 1:
        return data
    pivot = data[0]
    left = []
    right = []
    for x in range(1, len(data)):
        if data[x] <= pivot:
            left.append(data[x])
        else:
            right.append(data[x])
    left = quicksort(left)
    right = quicksort(right)
    foo = [pivot]
    return left + foo + right

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

    marmores = quicksort(marmores)

    print('CASE# {}:'.format(case))

    for consulta in range(q):
        valor = consultas[consulta]
        try:
            print('{} found at {}'.format(valor,marmores.index(valor)+1))
        except:
            print('{} not found'.format(valor))