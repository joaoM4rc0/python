"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
import re
import sys
cpf = input('digite seu cpf: ')
contador_regressivo = 10
contador_regressivo_novo = 11
resultado = 0
resultado_novo = 0
primeiro_digito = 0
segundo_digito = 0 

cpf_e_sequencial = cpf == cpf[0] * len(cpf)
if cpf_e_sequencial:
    print('você enviou dados sequenciais')
    sys.exit()
    
cpf = re.sub(
    r'[^0-9]',
    '',
    cpf
    )
nove_digitos = cpf[:9]
nove_digitos_limpo = nove_digitos
dez_digitos = cpf[:10]
    
for digito in nove_digitos:
    resultado += int(digito) * contador_regressivo
    contador_regressivo -= 1 
    if contador_regressivo == 1:
        primeiro_digito = (resultado * 10) % 11
        primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0 
        break

for digito in dez_digitos:
    resultado_novo += int(digito) * contador_regressivo_novo
    contador_regressivo_novo -= 1 
    if contador_regressivo_novo == 1:
        segundo_digito = (resultado_novo * 10) % 11
        segundo_digito = segundo_digito if segundo_digito <= 9 else 0
        break

cpf_gerado_calculo = f'{nove_digitos_limpo}{primeiro_digito}{segundo_digito}' 
if cpf == cpf_gerado_calculo:
    print('CPF VALIDO!')
else:
    print('CPF INVALIDO!')
print(primeiro_digito)
print(segundo_digito)

