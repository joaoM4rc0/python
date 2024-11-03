try:
    a = 18
    b = 2
    c = a/b 
    print(c)
except ZeroDivisionError:
    print('tentou dividir por zero')
except NameError:
    print('Nome b não está definido')
except (TypeError, IndexError) as error:
    print('TypeError + IndexError: ', error)
except Exception:
    print('ERRO DESCONHECIDO.')

print('CONTINUAR')