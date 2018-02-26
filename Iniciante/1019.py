total = int(input())

hora,total = divmod(total,3600)
minuto,segundo = divmod(total,60)

print('{}:{}:{}'.format(hora,minuto,segundo))