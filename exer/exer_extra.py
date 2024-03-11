
perguntas = [
    {
        'Pergunta': 'quem é o melhor meia do brasil atualmente?',
        'Opções': ['arrascaeta', 'garro', 'veiga', 'lucas'],
        'Resposta': 1,
    },
    {
        'Pergunta': 'quem é o melhor?',
        'Opções': ['mosquito', 'luan', 'jhon jhon', 'pelé'],
        'Resposta': 3,
    },
    {
        'Pergunta': 'quem joga mais no brasil?',
        'Opções': ['hulk', 'arrascaeta', 'gabi', 'lucas','veiga','luciano', 'garro'],
        'Resposta': 1,
    },
    {
        'Pergunta': 'quem é melhor?',
        'Opções': ['messi', 'neymar', 'cr7', 'yuri alberto'],
        'Resposta': 3,
    },
    {
        'Pergunta': 'quem está jogando mais no corinthians?',
        'Opções': ['yuri', 'raniele', 'garro', 'romero', 'wesley'],
        'Resposta': 2,
    },
    {
        'Pergunta': 'Qual a capacidade atual do Morumbi?',
        'Opções': ['68.576', '66.795', '59.628', '71.423'],
        'Resposta': 1,
    }
]
def jogo():
    acertos = 0 
    for pergunta in perguntas:
        print(f'pergunta: {pergunta['Pergunta']}')
        print()
        opcoes = pergunta['Opções']
        for i, opcao in enumerate(opcoes):
          print(f'{i})', opcao)  
        print()
        resposta = int(input('escolha a opção certa: '))
        if resposta == pergunta['Resposta']:
           print('voce acertou')
           acertos +=1
        else:
           print('voce errou')
    print(f'voce acertou {acertos} perguntas')
jogo()