class  Caneta:
    def __init__(self, cor):
        self.cor_usada = cor
    @property
    def cor(self):
        return self.cor_usada
    @property
    def cor_tampa(self):
        return 'verde'
cor = Caneta('azul')
print(cor.cor)
print(cor.cor_tampa)
print(cor.cor)
print(cor.cor)
print(cor.cor)
print(cor.cor)
print(cor.cor)