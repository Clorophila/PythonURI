n = int(input())
for k in range(n):
    original = input()

    string1 = ''
    for caracter in original:
        if caracter.isalpha():
            string1 = string1 + chr(ord(caracter) + 3)
        else:
            string1 = string1 + caracter

    string2 = ''.join(reversed(string1))

    string3 = string2[0:len(string2)//2]
    for i in range((len(string2)//2),len(string2)):
        string3 = string3 + chr(ord(string2[i]) - 1)

    print('{}'.format(string3))