a, b, c = map(int,input().split())

numeros = [a,b,c]

for num in sorted(numeros):
    print(num)
print('')
for num in numeros:
    print(num)