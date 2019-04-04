jogadas = {
    'tesoura':['papel','lagarto'],
    'papel':['spock','pedra'],
    'pedra':['lagarto','tesoura'],
    'lagarto':['spock','papel'],
    'spock':['tesoura','pedra'],
}
for c in range(int(input())):
    raj , sheldon = input().split()
    if raj == sheldon:
        print('empate')
    elif sheldon in jogadas[raj]:
        print('rajesh')
    else:
        print('sheldon')