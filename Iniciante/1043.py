a, b, c = map(float,input().split())

lados = [a,b,c]

if 2*max(lados)<sum(lados):
    print('Perimetro = {:.1f}'.format(sum(lados)))
else:
    print('Area = {:.1f}'.format(((a+b)/2)*c))