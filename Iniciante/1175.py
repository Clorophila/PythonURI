numeros = []
for case in range(20):
    numeros.append(int(input()))
numeros.reverse()
for i in range(20):
    print('N[{}] = {}'.format(i,numeros[i]))