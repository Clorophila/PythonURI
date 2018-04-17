n=int(input())
idades = []
while(n>=0):
    idades.append(n)
    n=int(input())
print('{:.2f}'.format(sum(idades)/len(idades)))