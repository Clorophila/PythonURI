T = 12
op = input()

mat = []
soma = 0

for l in range(T):
    aux = []
    for c in range(T):
        aux.append(float(input()))
        if(c<(T-l-1)):
            soma+=aux[c]
    mat.append(aux)

if(op=='S'):
    print('{:.1f}'.format(soma))
else:
    print('{:.1f}'.format(soma/((T*(T-1))/2)))