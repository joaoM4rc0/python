def contrutora(max = 10):
    for i in range(100000):
        yield i 

        if i >= max:
            return 

func = contrutora(50)
for valor in func:
    print(valor)