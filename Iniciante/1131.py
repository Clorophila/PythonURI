inter = 0
gremio = 0
empate = 0
n = 0

while(True):
    i,g = map(int,input().split())
    if(i>g):
        inter+=1
    elif(i<g):
        gremio+=1
    else:
        empate+=1
    n+=1
    print('Novo grenal (1-sim 2-nao)')
    if(input()=='2'):
        break

print('{} grenais'.format(n))
print('Inter:{}'.format(inter))
print('Gremio:{}'.format(gremio))
print('Empates:{}'.format(empate))
if(inter>gremio):
    print('Inter venceu mais')
elif(gremio>inter):
    print('Gremio venceu mais')
else:
    print('Nao houve vencedor')