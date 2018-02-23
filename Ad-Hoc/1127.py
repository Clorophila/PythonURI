semitons = {
    'A#':'b',
    'Bb':'b',
    'C#':'e',
    'Db':'e',
    'D#':'g',
    'Eb':'g',
    'F#':'j',
    'Gb':'j',
    'G#':'l',
    'Ab':'l',
    'B#':'d',
    'Fb':'h',
    'E#':'i',
    'Cb':'c',
    }

tons = {
    'A':'a',
    'B':'c',
    'C':'d',
    'D':'f',
    'E':'h',
    'F':'i',
    'G':'k',
    ' ':'',
    }

while True:
    if input()=='0 0':
        break
    else:        
        musica = input()
        trecho = input()
        for a, b in semitons.items():
            musica = musica.replace(a,b)
            trecho = trecho.replace(a,b)
        for a, b in tons.items():
            musica = musica.replace(a,b)
            trecho = trecho.replace(a,b)
        n = 0
        plagio = False
        while(n<12):
            if trecho in musica:
                plagio = True
                break
            else:
                acima = ''.join(chr(ord(i) + 1) for i in trecho)
                trecho = acima.replace('m','a')                
                n+=1
        if plagio:
            print('S')
        else:
            print('N')