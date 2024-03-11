x = 1
def escopo():
    # global x 
    x = 10
    def outra_funcao():
        x = 11
        y = 1
        print('outra_funcao',x,y)
    outra_funcao()
    print('escopo',x)
print(x)
escopo()
print(x)
