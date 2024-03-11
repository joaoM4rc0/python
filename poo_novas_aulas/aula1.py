
class Pessoa :
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
p1 = Pessoa('joao', 'marco', 19)
print(p1.nome)