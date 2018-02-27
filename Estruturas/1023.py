cidade = 0
controle = []
for i in range(201):
    controle.append(0)

while True:
    for i in range(201):
        controle[i]=0
    n = int(input())
    if(n==0):
        break
    cidade += 1
    consumo_total = 0
    pessoas_total = 0
    for i in range(n):
        pessoas, consumo = input().split()
        pessoas = int(pessoas)
        consumo = int(consumo)
        consumo_total += consumo
        pessoas_total += pessoas
        controle[consumo//pessoas] += pessoas
    print('Cidade# {}:'.format(cidade))
    for i in range(201):
        if(controle[i]!=0):
            print('{}-{}'.format(controle[i],i),end=' ')
    print('')
    consumo_medio = (int(100*(consumo_total/pessoas_total)))/100
    print('Consumo medio: {:.2f} m3.'.format(consumo_medio))
