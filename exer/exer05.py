numero = input('digite um número inteiro: ')

try :
    numero_Int = int(numero)
    numero_par = numero_Int % 2 == 0
    if numero_Int: 
        if numero_par: 
            print(f'{numero_Int} é par')
        else:
            print(f'{numero_Int} é impar')
except: 
    print('o número não foi digitado, ou ele não é um número inteiro')
