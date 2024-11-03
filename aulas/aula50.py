def decoradora(func):
    def aninhada(*args):
        resul = func(*args)
        return resul * 2
    return aninhada
@decoradora
def soma(x,y):
    return x + y
resultado = soma(2,2)
print(resultado)