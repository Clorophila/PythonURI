linha1 = input()
linha2 = input()

v1 = ''
v2 = ''

for c in linha1:
    if c in '0123456789.':
        v1 = v1 + c

for c in linha2:
    if c in '0123456789.':
        v2 = v2 + c

v1 = v1.split('.')
v2 = v2.split('.')

if len(v1[0])<=11:
    cpf = v1[0]
    v1[0] = '0'*11
else:
    cpf = v1[0][:11]

v1.append('0')
v1.append('0')
v1[1] = v1[1] + '00'
v2.append('0')
v2.append('0')
v2[1] = v2[1] + '00'


valor1 = float(v1[0][11:] + '.' + v1[1][:2])
valor2 = float(v2[0] + '.' + v2[1][:2])

print('cpf '+cpf)
print('{:.2f}'.format(valor1+valor2))