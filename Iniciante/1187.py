T = 12
op = input()

mat = []
soma = 0
elementos = 0

for l in range(T):
    aux = []
    for c in range(T):
        aux.append(float(input()))
        if (c>l) and (c<(T-l-1)):
            soma+=aux[c]
            elementos+=1
    mat.append(aux)

if(op=='S'):
    print('{:.1f}'.format(soma))
else:
    print('{:.1f}'.format(soma/(elementos)))