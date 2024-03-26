class Contabancaria:
    def __init__(self, valor):
        self.valor = valor
    def depositar(self, valor):
        self.valor += valor
    def sacar(self, valor):
        if valor <= self.valor:
           self.valor -= valor
           print(f'{valor} sacado ')
        else:
            print('o valor a sacar tem que ser menor que sua conta bancaria{self.valor}')
pessoa1 = Contabancaria(1000)
pessoa1.depositar(300)
pessoa1.sacar(500)