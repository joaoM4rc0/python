def saudacao(msg):
    def saudar(nome):
        return f'{msg} {nome}'
    return saudar
falar_bom_dia = saudacao('bom dia')
for nome in ['joao', 'maria', 'joaquina']:
    print(falar_bom_dia(nome))