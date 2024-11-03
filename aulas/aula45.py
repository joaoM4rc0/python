# raise - lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions
def nao_aceita_zero(d):
    if d == 0:
        raise ZeroDivisionError('voce esta tentando dividir por zero')
    return True
def aceita_int_float(n):
    if not isinstance(n, (int, float)):
        raise TypeError(
            f'"{n}" deve ser int ou float'
            ,f'"{type(n)}" enviado'
        )
    return True
def divide(n,d):
    aceita_int_float(n)
    aceita_int_float(d)
    nao_aceita_zero(n)
    nao_aceita_zero(d)
    return n/d
print(divide(10,2))