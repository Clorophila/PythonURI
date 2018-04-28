T = 12
c = int(input())
op = input()

mat = []
soma = 0

for i in range(T):
    aux = []
    for j in range(T):
        aux.append(float(input()))
        if(j==c):
            soma+=aux[j]
    mat.append(aux)

if(op=='S'):
    print('{:.1f}'.format(soma))
else:
    print('{:.1f}'.format(soma/T))