numeros = []
for case in range(10):
    numeros.append(float(input()))
for i in range(10):
    if(numeros[i]<=10):
        print('A[{}] = {:.1f}'.format(i,numeros[i]))