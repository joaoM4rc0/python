class Ponto:
    def __init__(self, x,y):
        self.x = x
        self.y = y
    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return novo_x + novo_y
    def __gt__(self, other):
        resultado_x = self.x + self.x
        resultado_y = other.y + other.y
        return resultado_x > resultado_y
p1 = Ponto(8, 4)
p2 = Ponto(3, 5)
p3 = p1 + p2
print(f'p1 é maior que p2? {p1 > p2}')
print(p3)