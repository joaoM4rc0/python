'''
Classe Bola: Crie uma classe que modele uma bola:
Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor
'''
class Bola:
    def __init__(self, cor, circuferencia, material):
        self.__cor = cor
        self.circuferencia = circuferencia
        self.material = material

    def trocar_cor(self, cor):
        self.__cor = cor

    def mostra_cor(self):
        return self.__cor

bola = Bola('red', 10, 'papel')
bola.trocar_cor('blue')
print(bola.mostra_cor())