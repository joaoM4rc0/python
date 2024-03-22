class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    def falar_nome_classe(self):
        print('classe PESSOA')
        print(self.nome, self.sobrenome, self.__class__.__name__)
class Cliente(Pessoa):
    def falar_nome_classe(self):
        print('eita, nem sai da classe CLIENTE')
        print(self.nome, self.sobrenome, self.__class__.__name__)
class Aluno(Pessoa):
    ...
c1 = Cliente('joao', 'santos')
c1.falar_nome_classe()
a1 = Aluno('maria', 'antonia')
a1.falar_nome_classe()