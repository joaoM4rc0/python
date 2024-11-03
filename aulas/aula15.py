qtn_linha = 5
qtn_coluna = 5

linha = 1

while linha <= qtn_linha:
    coluna=1
    while coluna <= qtn_coluna:
        print(f'{linha=} {coluna=}')
        coluna+= 1
    linha += 1

print('acabou')