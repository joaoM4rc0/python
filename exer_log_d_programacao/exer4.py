'''
Escreva um programa em Python que encontre números entre 2000 e 3200 
(inclusive) que sejam divisíveis por 7,
mas não sejam múltiplos de 5. 
Exiba esses números em uma sequência separada 
por vírgulas em uma única linha.'''

for i in range(2000, 3201): 
    if i % 7 == 0 and i % 5 == 1:
        print(i)