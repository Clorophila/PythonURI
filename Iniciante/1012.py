PI = 3.14159
a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

print('TRIANGULO: {:.3f}'.format((a*c)/2))
print('CIRCULO: {:.3f}'.format(PI*(c**2)))
print('TRAPEZIO: {:.3f}'.format(((a+b)/2)*c))
print('QUADRADO: {:.3f}'.format(b**2))
print('RETANGULO: {:.3f}'.format(a*b))