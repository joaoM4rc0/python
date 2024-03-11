class Carro :
    def __init__(self, nome, cor) :
        self.nome = nome
        self.cor = cor
    def acelerando(self):
        print(f'o carro {self.nome} da cor {self.cor} está acelerando')
car1 = Carro('civic type r', 'vermelha')
car1.acelerando()
car2 = Carro('civic', 'prata')
Carro.acelerando(car2)