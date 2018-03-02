def busca_binaria(lista,item):
    inicio = 0
    final = len(lista)
    if lista[0]==item:
        return 0
    while inicio < final:
        meio = (inicio+final)//2
        if lista[meio] == item:
            break
        elif lista[meio] > item:
            final = meio - 1
        elif lista[meio] < item:
            inicio = meio + 1
    if lista[meio] == item:
        while lista[meio] == item:
            meio -= 1
        return meio+1
    else:
        raise ValueError

lista = [0,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,3]

print(lista)
print(busca_binaria(lista,0))

'''

print(busca_binaria(lista,1))
print(busca_binaria(lista,2))
'''