class Multiplicar:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args ,**kwargs):
        resultado = self.func(*args ,**kwargs)
        return resultado * 6
@Multiplicar
def soma(x,y):
    return x + y
conta = soma(2,4)
print(conta)