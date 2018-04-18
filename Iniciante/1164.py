n = int(input())
for casos in range(n):
    x = int(input())
    limite = (x//2)+1
    soma = 0
    for i in range(1,limite):
        if(x%i==0):
            soma+=i
    if(soma==x):
        print('{} eh perfeito'.format(x))
    else:
        print('{} nao eh perfeito'.format(x))