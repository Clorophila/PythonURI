t = int(input())
base = []
for i in range(t):
    base.append(i)
vetor = base * (1000//(t-1))
for i in range(1000):
    print('N[{}] = {}'.format(i,vetor[i]))