m, n = map(int,input().split())
while(m>0 and n>0):
    soma = 0    
    if(n<m):
        for i in range(n,m+1):
            print(i,end=' ')
            soma += i
        print('Sum={}'.format(soma))
    else:
        for i in range(m,n+1):
            print(i,end=' ')
            soma += i
        print('Sum={}'.format(soma))
    m, n = map(int,input().split())