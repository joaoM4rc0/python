def decoradora(func):
    def aninhada(*args):
        resul = func(*args)
        return resul * 2
    return aninhada

@decoradora
def soma(x,y):
    return x + y
resultado = soma(5,10)
print(resultado)
resultado = soma(50,30)
print(resultado)
resultado = soma(577,1550)
print(resultado)