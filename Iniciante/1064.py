numeros = [float(input()) for x in range(6)]
positivos = []
for n in numeros:
    if n>0:
        positivos.append(n)

print('{} valores positivos'.format(len(positivos)))
print('{:.1f}'.format(sum(positivos)/len(positivos)))