class Conta:
    def __init__(self, valor, valor2):
        self.valor = valor
        self.valor2 = valor2
    @property
    def multiplicação(self):
        return self.valor * self.valor2
    @property
    def soma(self):
        return self.valor + self.valor2
    @property
    def subtracao(self):
        return self.valor - self.valor2
conta = Conta(50, 30)
print(conta.multiplicação)