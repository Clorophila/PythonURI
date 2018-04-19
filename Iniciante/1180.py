numeros = []
for case in range(100):
    numeros.append(int(input()))
print(max(numeros))
print(1+numeros.index(max(numeros)))