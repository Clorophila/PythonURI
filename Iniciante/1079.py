n = int(input())
for cases in range(n):
    a1, a2, a3 = map(float,input().split())
    print('{:.1f}'.format(((2*a1)+(3*a2)+(5*a3))/10.0))