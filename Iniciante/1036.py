a, b, c = map(float,input().split())

delta = (b**2)-(4*a*c)

if (delta < 0) or (a==0):
    print('Impossivel calcular')
elif delta == 0:
    raiz = (-b)/(2*a)
    print('R1 = {:.5f}'.format(raiz))
    print('R2 = {:.5f}'.format(raiz))
else:
    r1 = (-b+((delta)**(0.5)))/(2*a)
    r2 = (-b-((delta)**(0.5)))/(2*a)
    print('R1 = {:.5f}'.format(r1))
    print('R2 = {:.5f}'.format(r2))