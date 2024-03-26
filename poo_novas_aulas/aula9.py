class Foo:
    def __init__(self):
        self.__privado = 'isso é privado'
    def _method_privado(self):
        print(self.__privado)
        return 'acessando o metodo privado'
p = Foo()
print(p._method_privado())