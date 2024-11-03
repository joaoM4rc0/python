# lista_a = [1,2,3,4]
# lista_b = [5,6,7,8]
# lista_c = lista_a + lista_b
# print(lista_c)

nome = ['luiz', 'joao', 'marcela']
copy_list_nome = nome.copy()
nome[1] = 'eduardo'
print(copy_list_nome)
print(nome)

lista_a = ['luiz ']
lista_b = lista_a
lista_a[0] = 'joao'
print(lista_b)