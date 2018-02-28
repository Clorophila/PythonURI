tabela = {
    1:4.0,
    2:4.5,
    3:5.0,
    4:2.0,
    5:1.5,
}

item,quantidade = input().split()
item = int(item)
quantidade = int(quantidade)

print('Total: R$ {:.2f}'.format(tabela[item]*quantidade))