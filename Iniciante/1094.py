casos = int(input())
total = 0
coelhos = 0
ratos = 0
sapos = 0

for i in range(casos):
    num, tipo = input().split()
    total += int(num)
    if tipo == 'C':
        coelhos += int(num)
    elif tipo == 'R':
        ratos += int(num)
    else:
        sapos += int(num)

print('Total: {} cobaias'.format(total))
print('Total de coelhos: {}'.format(coelhos))
print('Total de ratos: {}'.format(ratos))
print('Total de sapos: {}'.format(sapos))
print('Percentual de coelhos: {:.2f} %'.format(100*(coelhos/total)))
print('Percentual de ratos: {:.2f} %'.format(100*(ratos/total)))
print('Percentual de sapos: {:.2f} %'.format(100*(sapos/total)))