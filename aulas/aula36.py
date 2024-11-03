letras = set()
while True:
    letra = input('digite uma letra: ')
    letras.add(letra.lower())

    if 'l' in letras:
        print('parabens')
        break
    print(letras)