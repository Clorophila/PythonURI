fibo = []
fibo.append(0)
fibo.append(1)
for i in range(2,61):
    fibo.append(fibo[i-1]+fibo[i-2])

cases = int(input())
for case in range(cases):
    n = int(input())
    print('Fib({}) = {}'.format(n,fibo[n]))