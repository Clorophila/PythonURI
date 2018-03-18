numeros = [int(input()) for x in range(5)]

print('{} valor(es) par(es)'.format(sum([1 if n%2==0 else 0 for n in numeros])))
print('{} valor(es) impar(es)'.format(sum([1 if n%2!=0 else 0 for n in numeros])))
print('{} valor(es) positivo(s)'.format(sum([1 if n>0 else 0 for n in numeros])))
print('{} valor(es) negativo(s)'.format(sum([1 if n<0 else 0 for n in numeros])))