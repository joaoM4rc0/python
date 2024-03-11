# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
#e listas na ordm.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
def une_cidades_estados(cidade, estado):
    nova_lista = []
    for cidades, estados in zip(cidade, estado):
        nova_lista.append((cidades , estados))
    return nova_lista
def cidades():
    cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
    return cidades

def estados():
    estados = ['BA', 'SP', 'MG', 'RJ']  
    return estados

uniao_estados_cidades = une_cidades_estados(cidades(), estados())
print(uniao_estados_cidades)

'''
outra forma de fazer 
from itertools import zip_longest

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']
print(list(zip(l1, l2)))
print(list(zip_longest(l1, l2, fillvalue='SEM CIDADE')))'''