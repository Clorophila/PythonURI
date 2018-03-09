a, b = map(int,input().split())

dur = ((b+24)-a)%24

print('O JOGO DUROU {} HORA(S)'.format(dur+24 if dur==0 else dur))