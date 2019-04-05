for caso in range(int(input())):
    valorhash = 0
    for linha in range(int(input())):
        entrada = input()
        for i in range(len(entrada)):
            valorhash += linha + i + ord(entrada[i]) - ord('A')
    print(valorhash)