e,d=map(int,input().split())

if e>d:
    print('Eu odeio a professora!')
elif e<(d-2):
    print('Muito bem! Apresenta antes do Natal!')
else:
    print('Parece o trabalho do meu filho!')
    if (e+2)<24:
        print('TCC Apresentado!')
    else:
        print('Fail! Entao eh nataaaaal!')