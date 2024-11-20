'''
Classe Quadrado: 
Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado,
 Retornar valor do Lado e calcular Área;
'''

class  Quadrado:
    def __init__(self, tamanho_do_lado, altura):
        self.lado = tamanho_do_lado
        self.altura = altura
    @property
    def tamanho_do_lado(self):
        return self.lado * self.altura
quadrado = Quadrado(50, 20)
print(quadrado.tamanho_do_lado)