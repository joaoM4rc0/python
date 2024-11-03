# def soma(x,y,z=0):
#     return x + y
# conta = soma(5, 8)
# print(conta)
x = input('digite um número para uma conta: ')
z = input('digite um número para uma conta: ')
y = input('digite um número para uma conta: ')
if x == '':
    x = None
def conta(x,z=0,y=0):
    z = int(z)
    y = int(y)
    if x is None:
        print(y -z)
    else: 
        x = int(x)
        print((x+z) * y) 
conta(x, z, y)