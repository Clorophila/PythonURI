t = int(input())
for casos in range(t):
    pa,pb,g1,g2=map(float,input().split())
    pa = int(pa)
    pb = int(pb)
    g1 = g1/100
    g2 = g2/100
    ano = 0
    while(pa<=pb and ano<=100):
        ano+=1
        pa += int(pa*g1)
        pb += int(pb*g2)
    if(ano>100):
        print('Mais de 1 seculo.')
    else:
        print('{} anos.'.format(ano))