x, y = map(float,input().split())

if x==0:
    if y==0:
        print('Origem')
    else:
        print('Eixo Y')
elif x>0:
    if y==0:
        print('Eixo X')
    elif y>0:
        print('Q1')
    else:
        print('Q4')
else:
    if y==0:
        print('Eixo X')
    elif y>0:
        print('Q2')
    else:
        print('Q3')