

while True:
    numero_um = input('digite um número: ')
    numero_dois = input('digite outro número: ')
    operador = input('qual operador voce escolhe para a conta? (/*-+) ')

    numeros_validos = None
    operadores_permitidos = '/*-+'

    try:
        float_num_um = float(numero_um)
        float_num_dois = float(numero_dois)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('os números nao foram digitados')
        continue

    if operador not in operadores_permitidos: 
        print('o operador não é permitido')
        continue
    
    if len(operador) > 1:
        print('só é permitido um operador')
        continue

    if operador == '/':
        conta = float_num_um / float_num_dois 
        print(f'{conta=}')

    if operador == '*':
        conta = float_num_um * float_num_dois 
        print(f'{conta=}')

    if operador == '-':
        conta = float_num_um - float_num_dois 
        print(f'{conta=}')

    if operador == '+':
        conta = float_num_um + float_num_dois 
        print(f'{conta=}')
  

    sair = input('voce quer sair? ([S])').lower().startswith('s')
    if sair is True: break