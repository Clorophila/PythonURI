categoria1 = input()
categoria2 = input()
categoria3 = input()

if categoria1 == 'vertebrado':
    if categoria2 == 'ave':
        if categoria3 == 'carnivoro':
            print('aguia')
        else:
            print('pomba')
    else:
        if categoria3 == 'onivoro':
            print('homem')
        else:
            print('vaca')
else:
    if categoria2 == 'inseto':
        if categoria3 == 'hematofago':
            print('pulga')
        else:
            print('lagarta')
    else:
        if categoria3 == 'hematofago':
            print('sanguessuga')
        else:
            print('minhoca')

    