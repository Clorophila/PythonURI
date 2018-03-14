hi, mi, hf, mf = map(int,input().split())

duracao_total = ((((hf+24)*60)+mf) - ((hi*60)+mi))%1440

if duracao_total == 0:
    h = 24
    m = 0
else:
    h = duracao_total//60
    m = duracao_total%60

print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(h,m))