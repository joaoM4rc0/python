primeiro_nome = input('escreva o seu primeiro nome: ')
largura_curta = len(primeiro_nome) <= 4
largura_media = len(primeiro_nome) >= 5 and len(primeiro_nome) <= 6
largura_longa = len(primeiro_nome) > 6 
if largura_curta:
    print('seu nome é curto')
elif largura_media:
    print('seu nome é normal')
elif largura_longa:
    print('seu nome é longo')

