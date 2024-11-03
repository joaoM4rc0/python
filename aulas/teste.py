novo_arquivo = 'C:\\Users\\joaom\\nova pasta teste\\'
novo_arquivo += 'teste.txt'

i = 0
while i <= 10:
    i+=1
nomes = ['joao', 'maria']
with open(novo_arquivo, 'w', encoding='utf-8') as arquivo:
    arquivo.write('isso veio do nada, \n')
    arquivo.write('vai se fuder , \n')
    arquivo.write('chico moedas é foda, \n')
    arquivo.write(f'{i} \n')
    arquivo.write(f'{nomes}')

with open(novo_arquivo, 'r') as arquivo:
    print (arquivo.read())
