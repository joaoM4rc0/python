'''
João Papo-de-Pescador, homem de bem,
comprou um microcomputador para controlar
o rendimento diário de seu trabalho. 
Toda vez que ele traz um peso de peixes maior que o estabelecido
pelo regulamento de pesca do estado de São Paulo (50 quilos)
deve pagar uma multa de R$ 4,00 por quilo excedente.
João precisa que você faça um programa que leia a variável
peso (peso de peixes) e calcule o excesso. 
Gravar na variável excesso, a quantidade de quilos além do limite
e na variável multa o valor da multa que João deverá pagar. 
Imprima os dados do programa com as mensagens adequadas.
'''
class Peixes:
    def __init__(self):
        self.peso_max = 50
        self.peso_peixe = 0
    @property
    def excesso(self):
        return self.peso_peixe
    @excesso.setter
    def peso(self, *peso):
        for peso_novo in peso:
            self.peso_peixe = peso_novo
            if peso_novo > self.peso_max:
                excesso_de_peso = peso_novo - self.peso_max
                multa = 4 * excesso_de_peso
                self.peso_peixe += multa
    def exibir(self):
        print(self.peso)
peixe = Peixes()
peixe.peso= 100
peixe.exibir()