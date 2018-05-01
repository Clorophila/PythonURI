cases = int(input())
for case in range(cases):
    n = int(input())
    if(n == 0):
        print('NULL')
    elif(n>0):
        if(n%2==0):
            print('EVEN POSITIVE')
        else:
            print('ODD POSITIVE')
    else:
        if((-n)%2==0):
            print('EVEN NEGATIVE')
        else:
            print('ODD NEGATIVE')