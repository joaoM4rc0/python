class Funcionario:
    def __init__(self, nome):
        self.nome = nome
        
class Empresa:
    def __init__(self):
        self.funcionarios = []
    
    def contratar(self, *nome):
        self.funcionarios += nome
    def exibir(self):
        print('funcionarios: ')
        for funcionario in self.funcionarios:
            print(f' - {funcionario}')
funcionario1 = Funcionario('joao')
funcionario2 = Funcionario('marco')
funcionario3 = Funcionario('maria')
empresa = Empresa()
empresa.contratar(funcionario1.nome)
empresa.contratar(funcionario2.nome)
empresa.contratar(funcionario3.nome)
empresa.exibir()