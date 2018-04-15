fibo = []
fibo.append(0)
fibo.append(1)
for i in range(2,47):
    fibo.append(fibo[i-1]+fibo[i-2])

n = int(input())
for i in range(n):
    if(i==(n-1)):
        print(fibo[i])
    else:
        print(fibo[i],end=' ')