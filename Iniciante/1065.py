pares = sum([1 if n%2==0 else 0 for n in [int(input()) for x in range(5)]])

print('{} valores pares'.format(pares))