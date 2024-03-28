class A:
    def __init__(self, argumento):
        self.argumento = argumento
    def metodo(self):
        print('A')
class B(A):
    def __init__(self, argumento, qualquer_coisa):
        self.coisas = qualquer_coisa
        super().__init__(argumento)
    def metodo(self):
        super().metodo()
        print('B')
class C(B):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('eu sou o c')
    def metodo(self):
        super().metodo()
        print('C')
c = C('olá', 'qualquer coisa')
c.metodo()
