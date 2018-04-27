T = 12
l = int(input())
op = input()

mat = []

for i in range(T):
    aux = []
    for j in range(T):
        aux.append(float(input()))
    mat.append(aux)

if(op=='S'):
    print('{:.1f}'.format(sum(mat[l])))
else:
    print('{:.1f}'.format(sum(mat[l])/T))