"""
Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer.]
Obs: Por padrão, a cada ano que nossa pessoa envelhece,
sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
"""
class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self._nome = nome
        self._idade = idade
        self._peso = peso
        self._altura = altura
    @property
    def idade(self):
        return self._idade
    @property
    def altura(self):
        return self._altura
    @property
    def peso(self):
        return self._peso
    @idade.setter
    def envelhecer(self, valor):
        if self._idade <= 21:
            self._altura += 0.05
            self._idade += valor
        else:
            self._idade += valor
    @peso.setter
    def engordar(self, valor):
        self._peso += valor
    @peso.setter
    def emagrecer(self, valor):
        self._peso -= valor
pessoa = Pessoa('Joao', 18, 84, 1.80)
pessoa.envelhecer = 2
pessoa.engordar = 5
pessoa.emagrecer = 10
print(pessoa.idade, pessoa.altura, pessoa.peso) 