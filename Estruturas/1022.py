casos = int(input())

for n in range(casos):
    entrada = input().split()
    n1 = int(entrada[0])
    d1 = int(entrada[2])
    n2 = int(entrada[4])
    d2 = int(entrada[6])
    if(entrada[3]=='+'):
        n = (n1*d2 + n2*d1)
        d = d1*d2
    elif(entrada[3]=='-'):
        n = (n1*d2 - n2*d1)
        d = d1*d2
    elif(entrada[3]=='*'):
        n = n1*n2
        d = d1*d2
    else:
        n = n1*d2
        d = n2*d1
    mdc = 1
    for i in range(1,min(abs(n),abs(d))+1):
        if(n%i==0 and d%i==0):
            mdc = i

    print('{}/{} = {}/{}'.format(n,d,n//mdc,d//mdc))