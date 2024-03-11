#Filtrando elementos pares de um vetor de inteiros: Suponha que temos um vetor de números inteiros:
#List Comprehension
import random

import copy
lista = []
for numeros in range(0,10):
    lista.append(random.randint(0,50))

nova_lista = sorted([copy.deepcopy(x) for x in lista])
print(lista)
print()
print(nova_lista)