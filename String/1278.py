import re
first = True
while True:
    linhas = int(input())
    texto = []
    maior = 0
    if linhas == 0:
        break
    else:
        if not first:
            print()
        for l in range(linhas):
            linha = re.sub(r'\s+',' ', input().strip())
            texto.append(linha)
            if len(linha) > maior:
                maior = len(linha)
        for l in texto:
            print('{0:>{1}}'.format(l,maior))
        first = False