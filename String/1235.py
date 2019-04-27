for c in range(int(input())):
    entrada = input()
    t = len(entrada)
    resposta = ''.join(reversed(entrada[(t//2):t]+entrada[0:(t//2)]))
    print(resposta)