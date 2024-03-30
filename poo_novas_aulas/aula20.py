class Ponto:
    def __init__(self,x ,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        classe_nome = __class__.__name__
        return f'{classe_nome}{self.x, self.y, self.z}'
p1 = Ponto(5,8,'olá')
print(p1)