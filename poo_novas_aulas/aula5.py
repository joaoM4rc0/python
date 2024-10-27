class Animal:
    tipo = 'animal'
    def __init__(self, nome, familia):
        self.nome = nome
        self.familia = familia
    @classmethod
    def cria_animal(cls, nome, familia):
        return f'o nome do seu animal é {nome}, e sua familia é a {familia}'
animal = Animal.cria_animal('gato', 'felideos')
print(animal)
animal2 = Animal.cria_animal('cachorro', 'canideos')
print(animal2)