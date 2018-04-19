vetor = []
for i in range(10):
    k = int(input())
    if(k>0):
        vetor.append(k)
    else:
        vetor.append(1)
for i in range(10):
    print('X[{}] = {}'.format(i,vetor[i]))