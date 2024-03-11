import os
import json
# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
CAMINHO_ARQUIVO = 'exer21.json'
lista = ler([], CAMINHO_ARQUIVO)
elemento_excluido =[]
while True: 
    def comandos():
        comando = input('comandos = listar, desfazer, refazer \n digite uma tarefa ou comando: ')
        verifica_comando(comando)

    def verifica_comando(comando):
        comando_permitido = ['listar', 'desfazer', 'refazer']
        if comando not in comando_permitido:
            if comando == 'clear':
                return os.system('cls')
            return adicionar_tarefa(comando)
        elif comando in comando_permitido and comando == 'desfazer':
            return desfaz_uma_tarefa()
        elif comando in comando_permitido and comando == 'listar':
            return listar_lista()
        elif comando in comando_permitido and comando == 'refazer':
            return refazer()
    def lista_de_tarefas(nome): 
            lista.append(nome)
            print('tarefas:')
            for valor in lista:
                print(valor)

    def adicionar_tarefa(tarefa):
        return lista_de_tarefas(tarefa)
    
    def desfaz_uma_tarefa():
        if len(lista) == 0:
            print('não existe mais elementos na sua lista')
        else:
            elemento_excluido.insert(0, lista.pop())
            for valor in lista:
                print(valor)

    def listar_lista():
        if len(lista) == 0:
            print('a lista está zerada, adcione elementos para conseguir ver')
        else:
            print(lista)
    def refazer() :
        for elemento in elemento_excluido:
            lista.append(elemento_excluido[len(elemento_excluido)- 1])
            elemento_excluido.pop(-1)
            print(elemento)
            break
    def ler(tarefas, caminho_arquivo):
        dados = []
        try:
            with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
                dados = json.load(arquivo)
        except FileNotFoundError:
            print('Arquivo não existe')
            salvar(tarefas, caminho_arquivo)
        return dados
    def salvar(tarefas, caminho_arquivo):
        dados = tarefas
        with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
            dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)
        return dados

    comandos()