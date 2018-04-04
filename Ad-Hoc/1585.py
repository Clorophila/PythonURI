casos = int(input())
for caso in range(casos):
    a, b = map(int,input().split())
    print('{} cm2'.format((a*b)//2))