valores = (100,50,20,10,5,2,1)
total = int(input())
print(total)
for valor in valores:
    notas,total = divmod(total,valor)
    print('{} nota(s) de R$ {},00'.format(notas,valor))