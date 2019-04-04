for case in range(int(input())):
    entrada = input()
    mensagem = ''
    for c in entrada:
        if c.islower():
            mensagem = c + mensagem
    print(mensagem)
