x, y = map(int,input().split())

for n in range(1,y+1):
    if(n%x==0):
        print(n)
    else:
        print(n,end=' ')