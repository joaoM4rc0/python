# condicao = True 
# while condicao:
#     nome = input('digite seu nome: ')
#     print(f'seu nome é {nome}')
#     break


# numero = 1 
# while numero < 10:
#     print(numero)
#     numero += 1


numero = 1 
condicao = True
while condicao:
    numero *= 2
    print(numero)
    if numero > 20: condicao = False