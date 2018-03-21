positivos = sum([1 if n>0 else 0 for n in [float(input()) for x in range(6)]])

print('{} valores positivos'.format(positivos))