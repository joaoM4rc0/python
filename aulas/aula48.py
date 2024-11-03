def concatenar(string_concatenar):
    valor_final = string_concatenar
    def interno(valor_a_concatenar):
        nonlocal valor_final
        valor_final += valor_a_concatenar        
        return valor_final
    return interno
c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))