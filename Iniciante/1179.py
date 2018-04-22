par = []
impar = []
for casos in range(15):
    s = 1
    n = int(input())
    if(n<0):
        s = -1
        n = -n
    if(n%2==0):
        par.append(n*s)
    else:
        impar.append(n*s)
    if(len(par)==5):
        for i in range(5):
            print('par[{}] = {}'.format(i,par[i]))
        par = []
    if(len(impar)==5):
        for i in range(5):
            print('impar[{}] = {}'.format(i,impar[i]))
        impar = []
for i in range(len(impar)):
    print('impar[{}] = {}'.format(i,impar[i]))
for i in range(len(par)):
    print('par[{}] = {}'.format(i,par[i]))