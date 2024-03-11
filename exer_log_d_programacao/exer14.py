#Removendo caracteres não numéricos de uma string: Suponha que temos uma string:
#List Comprehension
lista = 'abc1234def'
lista_nova = [char for char in lista if char.isdigit()]
print(lista_nova)