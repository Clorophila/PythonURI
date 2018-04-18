casos = int(input())
for caso in range(casos):
    soma = 0
    menor, maior = map(int,input().split())
    if menor > maior:
        menor, maior = maior, menor
    for num in range(menor+1,maior):
        if num%2==1:
            soma += num
    print(soma)