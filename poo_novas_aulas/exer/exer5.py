class Trabalhador:
    def __init__(self, nome_completo,idade, cpf, cargo):
        self.nome = nome_completo
        self.idade = idade
        self.cpf = cpf
        self.cargo = cargo
        self.__salario_funcionario = 0
        self.__hora_trabalhada = 0
        self.__cargo_horaria = 8

    def registrar_hora_trabalhada(self):
        self.__hora_trabalhada += 1 
    @property
    def salario(self):
        return self.__salario_funcionario
    @salario.setter
    def salario_valor(self, valor):
        if self.__hora_trabalhada < 8:
            print('voce não trabalhou o suficiente') 
        else:
            self.__salario_funcionario += 2000
            if self.__hora_trabalhada > 8 and self.__hora_trabalhada < 13:
                self.__salario_funcionario += 100
            print(f'seu salário é de {self.__salario_funcionario}')

pessoa = Trabalhador('joao marco santos andrade', 10,'100.174.125-08', 'programador')
i = 0
while i <= 15:
    pessoa.registrar_hora_trabalhada()
    i+=1

pessoa.salario_valor = None