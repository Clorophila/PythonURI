cod, num, v_unit = input().split()
cod1 = int(cod)
num1 = int(num)
v_unit1 = float(v_unit)

cod, num, v_unit = input().split()
cod2 = int(cod)
num2 = int(num)
v_unit2 = float(v_unit)

total = (num1*v_unit1) + (num2*v_unit2)

print('VALOR A PAGAR: R$ {:.2f}'.format(total))