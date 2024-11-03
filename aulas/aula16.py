numeros = 'aaooodddd'
i = 0
qtn_num_apareceu_mais = 0
qtn_vezes_letra_apareceu = ''
while i < len(numeros):
    numeros_atuais = numeros[i]

    if numeros_atuais == ' ':
        i +=1
        continue
    
    quantas_vezes_letra_apareceu = numeros.count(numeros_atuais)
    if qtn_num_apareceu_mais < quantas_vezes_letra_apareceu:
        qtn_num_apareceu_mais = quantas_vezes_letra_apareceu
        qtn_vezes_letra_apareceu =numeros_atuais 
    i += 1
print(qtn_vezes_letra_apareceu, qtn_num_apareceu_mais)