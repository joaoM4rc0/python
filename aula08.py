logar = input('[E]ntrar [S]air: ')

if logar == 'E' or logar == 'e':
    email = input('digite seu email: ') or print('sem email')
    senha = input('digite sua senha: ') or print('sem senha')

email_permitido = 'joaom@gmail.com'
senha_permitido = '123456'

if logar == 'S' or logar == 's':
    print('voce saiu')
elif email == email_permitido and senha == senha_permitido: 
    print('voce logou')
else: 
    print('deu ruim')

nome = input('digite um nome: ')
digite_oq_procura = input('digite uma letra: ')
if digite_oq_procura in nome: 
    print(f'{digite_oq_procura} pertence a {nome}')
else:
    print(f'{digite_oq_procura} não pertence a {nome}')