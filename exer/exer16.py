# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'quem é o melhor meia do brasil atualmente?',
        'Opções': ['arrascaeta', 'garro', 'veiga', 'lucas'],
        'Resposta': 'garro',
    },
    {
        'Pergunta': 'quem é o melhor?',
        'Opções': ['mosquito', 'luan', 'jhon jhon', 'pelé'],
        'Resposta': 'luan',
    },
    {
        'Pergunta': 'quem joga mais no brasil?',
        'Opções': ['hulk', 'arrascaeta', 'gabi', 'lucas','veiga','luciano', 'garro'],
        'Resposta': 'arrascaeta',
    },
    {
        'Pergunta': 'quem é melhor?',
        'Opções': ['messi', 'neymar', 'cr7', 'yuri alberto'],
        'Resposta': 'yuri alberto',
    },
    {
        'Pergunta': 'quem está jogando mais no corinthians?',
        'Opções': ['yuri', 'raniele', 'garro', 'romero', 'wesley'],
        'Resposta': 'raniele',
    },
    {
        'Pergunta': 'Qual a capacidade atual do Morumbi?',
        'Opções': ['68.576', '66.795', '59.628', '71.423'],
        'Resposta': 1,
    }
]
acertos = 0
for pergunta in perguntas:
    print(f'pergunta: {pergunta['Pergunta']}')
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', {opcao})
    print()

    escolha = input('escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtn_opcoes = len(opcoes)
    if escolha.isdigit():
        escolha_int = int(escolha)
    
    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int  < qtn_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True
    print()

    if acertou:
        acertos += 1 
        print('Acertou 👍')
    else:
        print('Errou ❌')
    print()

    
print(f'você acertou {acertos} questões')
print('de', len(perguntas), 'perguntas.')