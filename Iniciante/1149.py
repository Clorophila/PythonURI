soma = 0
leitura = list(map(int,input().split()))
a = leitura[0]
n = leitura[1]
i = 2
while(n<=0):
    n = leitura[i]
    i+=1

for i in range(a,n+a):
    soma+=i

print(soma)