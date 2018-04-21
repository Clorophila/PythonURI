numeros = []
for case in range(100):
    numeros.append(float(input()))
for i in range(100):
    if(numeros[i]<=10):
        print('A[{}] = {:.1f}'.format(i,numeros[i]))