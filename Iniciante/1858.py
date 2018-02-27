input()
pessoas = [int(n) for n in input().split()]

menor = pessoas[0]
num = 0
for indice,valor in enumerate(pessoas):
    if valor<menor:
        menor = valor
        num = indice

print('{}'.format(num+1))