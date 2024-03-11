'''
Cálculo do Volume de uma Esfera:
Crie um programa em Python
para calcular o volume de uma esfera 
com um diâmetro de 12 cm usando a fórmula:
(onde r é o raio da esfera).

Encontre o raio. Se você já o conhece, pule este Passo.
r = D/2, onde D é o diâmetro da esfera. (calculo para encontrar o raio)
Eleve o raio ao cubo.
Multiplique o raio elevado ao cubo por ⁴⁄₃.
Multiplique a equação por π.
A fórmula do volume da esfera é Ve = 4.п.r3/323.
'''
def encontra_volume(diametro):
    def encontra_raio():
        conta_raio = (((diametro/2) ** 3) * (4/3)) * 3.14
        return conta_raio
    return encontra_raio()
esfera = encontra_volume(12)
print(f'o valor do volume da esfera é {esfera}')