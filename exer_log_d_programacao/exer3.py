def calcula_idade_em_ano(idade):
    idade_int = int(idade)
    def calcula_mes():
        calc_mes = idade_int * 12
        print(calc_mes)
        return calc_mes
    calcula_ano = 2024 - idade_int
    return calcula_ano, calcula_mes()
idade = input('digite a sua idade: ')
resultado_ano, resultado_mes = calcula_idade_em_ano(idade)
print(f'{resultado_ano=} {resultado_mes=}')