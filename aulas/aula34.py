# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

import copy #faz uma copia profunda
d1 = {
    'd1': 1,
    'd2': 2,
    'l1': [1,2,3,4,5]
}
d1.update(nome='maria', idade=50)
# d1.pop('l1')
d2 = copy.deepcopy(d1) # com essa copia podemos modificar completamente o dicionario
# d2 = d1.copy() # não da para modificar lista por exemplo
print(d2)
