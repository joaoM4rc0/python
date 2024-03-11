#Obtendo o primeiro e o último nome a partir do nome completo:

nome_usuario = input('digite seu nome completo: ')
lista_nome = nome_usuario.split()
primeiro_nome = lambda nome: nome[0]
ultimo_nome = lambda nome: nome[-1]
print(f"Seu primeiro nome é {primeiro_nome(lista_nome)} e o seu último nome é {ultimo_nome(lista_nome)}")