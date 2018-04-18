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
            c=0
            v=0
            while(c<1 or c>2):
                print('novo calculo (1-sim 2-nao)')
                c = int(input())
            if(c==2):
                break