import json
pessoa = {
    'nome': 'joao marco',
    'sobrenome': 'santos',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

with open('aula56.json', 'w', encoding='utf-8') as arquivo:
    json.dump(
    pessoa,
    arquivo, 
    ensure_ascii=False,
    indent=2
    )
with open('aula56.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)

    print(pessoa['nome'])
