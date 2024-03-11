# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor

def conta(*args):
    numeros = 1
    for i in args:
        numeros *= i 
    print( numeros)
numeros = conta(1,2,3,4,5)

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def par_impar(x):
    valor = x
    if valor % 2 == 0:
        return f'{valor= } é par'
    return f'{valor= } é impar'
numero = par_impar(5)
print(numero)