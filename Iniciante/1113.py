while(True):
    m, n = map(int,input().split())
    if(m<n):
        print('Crescente')
    elif(m>n):
        print('Decrescente')
    else:
        break