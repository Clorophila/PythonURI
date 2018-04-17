n = int(input())
for k in range(n):
    x,y = map(int,input().split())
    if(x%2==0):
        x+=1
    soma = ((2*x+(y-1)*2)//2)*(y)
    print(soma)