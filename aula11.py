numero = input('digite um número: ')

try:
    numero_int = int(numero)
    print(numero_int * 2 )
except:
    print('isso não é um número')