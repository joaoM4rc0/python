import random
cpf = ''
for i in range(9):
    cpf += str(random.randint(0, 9))
contador_regressivo = 10
resultado = 0
primeiro_digito = 0
segundo_digito = 0 

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
    resultado = 0
    contador_regressivo = 11
    resultado += int(digito) * contador_regressivo
    contador_regressivo -= 1 
    if contador_regressivo == 1:
        segundo_digito = (resultado * 10) % 11
        segundo_digito = segundo_digito if segundo_digito <= 9 else 0
        break

cpf_gerado_calculo = f'{nove_digitos_limpo}{primeiro_digito}{segundo_digito}' 
print(cpf_gerado_calculo)