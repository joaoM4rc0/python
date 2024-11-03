texto ='omaigode'
i = 0
largura_texto = len(texto)
while i < largura_texto:
    texto_novo = texto[i]
    if texto_novo == ' ':
        i+=1
    print(texto_novo)
    i+=1