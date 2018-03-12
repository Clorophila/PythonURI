salario = float(input())

if salario <= 400:
    aumento = 15
elif salario <= 800:
    aumento = 12
elif salario <= 1200:
    aumento = 10
elif salario <= 2000:
    aumento = 7
else:
    aumento = 4

reajuste = salario*(aumento/100)

print('Novo salario: {:.2f}'.format(salario+reajuste))
print('Reajuste ganho: {:.2f}'.format(reajuste))
print('Em percentual: {} %'.format(aumento))