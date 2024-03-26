class Caneta:
    def __init__(self, cor, cor_tampa):
        self._cor = cor
        self._cor_tampa = cor_tampa
    @property
    def cor(self):
        print('GETTER')
        return self._cor
    @cor.setter
    def cor (self, valor):
        print('SETTER')
        self._cor = valor
    @property
    def cor_tampa(self):
        return self._cor_tampa
    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor
caneta = Caneta('blue', 'blue')
caneta.cor = 'rosa'
caneta.cor_tampa = 'red'
print(caneta.cor, caneta.cor_tampa)