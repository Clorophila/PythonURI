n1, n2, n3, n4 = map(float,input().split())

media = ((n1*2)+(n2*3)+(n3*4)+(n4*1))/(2+3+4+1)

print('Media: {:.1f}'.format(media))

if(media>=7):
    print('Aluno aprovado.')
elif(media<5):
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    exame = float(input())
    print('Nota do exame: {:.1f}'.format(exame))
    media_final = (media+exame)/2
    if(media_final>=5):
        print('Aluno aprovado.')
        print('Media final: {:.1f}'.format(media_final))
    else:
        print('Aluno reprovado.')
        print('Media final: {:.1f}'.format(media_final))