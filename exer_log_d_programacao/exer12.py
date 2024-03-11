#Obtendo a primeira letra de cada fruta: Suponha que temos uma lista de frutas:
#List Comprehension

frutas =  [ 'maçã', 'uva', 'pêra']
lista_com_inciais_das_frutas = [fruta[0] for fruta in frutas]
print(lista_com_inciais_das_frutas)