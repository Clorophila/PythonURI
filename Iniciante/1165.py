k = int(input())
for casos in range(k):
    n = int(input())
    top = int(n**(0.5))+1
    prime = True
    if(n%2==0 and n!=2):
        prime = False
    else:
        for d in range(3,top,2):
            if(n%d==0):
                prime = False
                break
    if(prime):
        print('{} eh primo'.format(n))
    else:
        print('{} nao eh primo'.format(n))