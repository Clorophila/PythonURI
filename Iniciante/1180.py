n = int(input())
numeros = list(map(int,input().split()))
print('Menor valor: {}'.format(min(numeros)))
print('Posicao: {}'.format(numeros.index(min(numeros))))