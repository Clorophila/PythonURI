a, b, c = reversed(sorted(map(float,input().split())))

if a>=(b+c):
    print('NAO FORMA TRIANGULO')
else:
    if (a**2) == ((b**2) + (c**2)):
        print('TRIANGULO RETANGULO')
    elif (a**2) > ((b**2) + (c**2)):
        print('TRIANGULO OBTUSANGULO')
    else:
        print('TRIANGULO ACUTANGULO')
    if a==b and b==c:
        print('TRIANGULO EQUILATERO')
    elif a==b or b==c or a==c:
        print('TRIANGULO ISOSCELES')