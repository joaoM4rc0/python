'''Inversão da Ordem do Nome do Usuário:
Desenvolva um programa que receba o primeiro e último nome do usuário
e, em seguida, imprima-os em ordem reversa,
separados por um espaço.'''

def inverte_nome(valor1):
        def nome_invertido():
                return valor1[::-1],
        return nome_invertido() 
nome = input('digite seu primeiro nome e seu ultimo nome: ')
valor = inverte_nome(nome)
print(*valor, )