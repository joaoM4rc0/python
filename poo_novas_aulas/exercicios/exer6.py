class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.professores = []
    def adicionar_professores(self, professor):
        self.professores.append(professor)
class Professor:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []
    def adicionar_alunos(self, aluno):
        self.alunos.append(aluno)
aluno1 = Aluno('joao')
aluno2 = Aluno('maria')
professor = Professor('zubervaldo')
professor2 = Professor('geronimo')
professor3 = Professor('jucilei')
aluno2.adicionar_professores(professor)
aluno2.adicionar_professores(professor2)
aluno2.adicionar_professores(professor3)
print(F'professores da {aluno2.nome}:')
for profe in aluno2.professores:
    print(f' -   {profe.nome}')
#Cada aluno tem uma lista de professores associados.
# Cada professor tem uma lista de alunos associados.