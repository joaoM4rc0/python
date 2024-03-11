nome_usuario = input('digite seu nome: ')
idade_usuario = input('digite sua idade: ')

if nome_usuario != '' and idade_usuario != '':
    print("seu nome e idade foram digitados") 
    print(f'seu nome é {nome_usuario}')
    print(f'seu nome invertido é {nome_usuario[::-1]}')

    if ' ' in nome_usuario:
        print('seu nome contém espaços')
        print(f'seu nome é {nome_usuario}')
    else:
        print('seu nome não contém espaços')

else: 
    print('seu nome ou idade não foram digitados')


if nome_usuario and idade_usuario:
    print(f'seu nome tem {len(nome_usuario)} letras ')
    print(f'a primeira letra do seu nome é {nome_usuario[0]}')
    print(f'a última letra do seu nome é {nome_usuario[-1]}')