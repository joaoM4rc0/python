def conta(*args):
    numeros = []
    for num in args:
        numeros.append(num) 
        print(numeros)

numeros = list(range(0,11))
conta(*numeros)