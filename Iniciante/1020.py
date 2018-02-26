total = int(input())

ano,total = divmod(total,365)
mes,dia = divmod(total,30)

print('{} ano(s)'.format(ano))
print('{} mes(es)'.format(mes))
print('{} dia(s)'.format(dia))