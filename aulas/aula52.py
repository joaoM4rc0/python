from functools import partial 
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)

aumenta_por_dez = partial(
    aumentar_porcentagem, 
    porcentagem = 1.1
)
aumenta_por_20 = partial(
    aumentar_porcentagem, 
    porcentagem = 1.2
)
def aumenta_preco():
    return True

def muda_preco_de_produto(produto):
        if aumenta_preco() == True and produto['preco'] > 50:
            return{**produto, 'preco':aumenta_por_dez(produto['preco'])}
        if aumenta_preco() == True and produto['preco'] < 50:
            return{**produto, 'preco':aumenta_por_20(produto['preco'])}
        
def novos_produtos():
    if aumenta_preco() != False: 
        novos_produtos = list(map(
            muda_preco_de_produto,
            produtos
        ))
        return novos_produtos
    else:
        return produtos
    
print(*novos_produtos(), sep='\n')
