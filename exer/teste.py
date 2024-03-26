class ContaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")
conta = ContaBancaria(1000)
conta.depositar(200)
conta.sacar(300)
print(conta.saldo)  # Saída: 900