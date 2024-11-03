def cria_funcao(func):
    def interna(*args):
        for arg in args:
            e_string(arg)
            resultado = func(*args)
            print(f'o seu resultado foi {resultado}')
            return resultado
    return interna
@cria_funcao
def inverte_str(string):
    print(inverte_str.__name__)
    return string[::-1]
def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')

invertida = inverte_str('123')
print(invertida)
