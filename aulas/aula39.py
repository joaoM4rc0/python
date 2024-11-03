# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
lista = [numero for numero in range(11)]
# print(lista)

# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'camisa', 'preco': 80,},
    {'nome': 'sapato', 'preco': 100,},
    {'nome': 'short', 'preco': 80,},
]
novos_produtos = [
    {**produto, 'preco': produto['preco'] *1.02}
    if produto['preco'] > 70 else {**produto}
    for produto in produtos
    if produto['preco'] >= 70 and produto['preco']  * 1.02 > 90
]
# print(*novos_produtos,sep='\n')

# filtrando 
lista = [n for n in range(10) if n <= 5]
# print(lista)
# lista = [] 
# for x in range(3):
#     for y in range(3):
#         lista.append((x,y))
# print(lista)
lista = [
    (x, y)
    for x in range(3)
    for y in range(3)
]
print(lista)
