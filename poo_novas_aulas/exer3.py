class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self.idade = idade
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nome):
        self._nome = nome
pessoa = Pessoa('joao', 18)
pessoa.nome = 'maria'
print(pessoa.nome)
