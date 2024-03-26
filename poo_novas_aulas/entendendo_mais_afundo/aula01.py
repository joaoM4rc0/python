class Conta:
    def __init__(self, valor):
        self.valor = valor
    def incrementa(self):
        self.valor += 1 
conta = Conta(0)
conta.incrementa()
i = conta.valor
while i <= 10:
    i = conta.valor
    print(i)
    conta.incrementa()