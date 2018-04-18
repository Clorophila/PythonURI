x = int(input())
y = int(input())

if(x>y):
    x,y=y,x

soma=0

for n in range(x,y+1):
    if(n%13==0):
        pass
    else:
        soma+=n

print(soma)