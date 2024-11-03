import sys
iterable = ['eu', 'gosto', 'do', 'neymar']
iterador = iter(iterable)
for nome in iterador:
    print(nome)
lista = [n for n in range(1000000)]
generator = (n for n in range(1000000))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

print(generator)