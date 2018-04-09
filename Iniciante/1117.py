v = 0
while(True):
    nota = float(input())
    if(nota<0 or nota>10):
        print('nota invalida')
    else:
        if(v==0):
            nota1=nota
            v=1
        else:
            print('media = {:.2f}'.format((nota1+nota)/2.0))
            break