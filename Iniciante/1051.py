salario = float(input())

if salario <= 2000:
    print('Isento')
elif salario <= 3000:
    print('R$ {:.2f}'.format(0+((salario-2000)*(0.08))))
elif salario <= 4500:
    print('R$ {:.2f}'.format(80+((salario-3000)*(0.18))))
else:
    print('R$ {:.2f}'.format(350+((salario-4500)*(0.28))))