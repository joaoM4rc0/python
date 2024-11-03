import os   
lista = []
while True:
    print('selecione uma opção')
    opcoes = input('[i]nserir [a]pagar [l]istar ').lower()
    opcoes_permitidas = 'ial'
    if opcoes not in opcoes_permitidas:
        print('não é possivel fazer nada')
    
    if opcoes == 'i':
        lista_add_item = input('adicione oq quiser na lista: ')
        lista.append(lista_add_item)
        for lista_enumerada in enumerate(lista):
            indice, nome = lista_enumerada
            print(indice, nome)
    if opcoes == 'a':
        lista_del_item = input('digite um indice para apagar: ')
        os.system('cls')
        try:
            int_lista = int(lista_del_item)
            if int_lista == indice:
                lista.pop(int_lista)
        except ValueError:
            print('digite um número')
        except NameError:
            print('você tem que adicionar um elemento a sua lista ')
        if int_lista > len(lista):
            print('esse índice não existe')
    if opcoes == 'l':
        if len(lista) == 0:
            os.system('cls')
            print('não tem nada para listar')
        for i, valor in enumerate(lista):
            print(i, valor)