for casos in range(int(input())):
    entrada = input()
    if len(entrada) > 3:
        print('3')
    else:
        dois = 0
        two = 'two'
        for i in range(3):
            if entrada[i] == two[i]:
                dois += 1
        if dois > 1:
            print('2')
        else:
            print('1')
