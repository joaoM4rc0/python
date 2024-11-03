from functools import reduce
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
def valor_reduce(acumulador, produto):
    return round(acumulador + produto['preco'],2)
total = reduce(
    valor_reduce, 
    produtos,
    0
)
print(total)