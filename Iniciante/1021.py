notas = (100,50,20,10,5,2)
moedas = (100,50,25,10,5,1)
total = float(input())

reais = int(total)
centavos = int((total-reais)*100)

print('NOTAS:')
for valor in notas:
    notas,reais = divmod(reais,valor)
    print('{} nota(s) de R$ {}.00'.format(notas,valor))

centavos += reais*100
print('MOEDAS:')
for valor in moedas:
    moedas,centavos = divmod(centavos,valor)
    print('{} moeda(s) de R$ {:.2f}'.format(moedas,valor/100))