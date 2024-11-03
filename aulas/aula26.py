class Mycall:
    def __init__(self, numero):
        self.phone = numero
    def __call__(self, nome):
        print(nome, 'está ligando', self.phone)
        return True 
call1 = Mycall('75965487563')
retorno = call1('joãozinho')
print(retorno)