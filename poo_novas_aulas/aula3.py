class Animal:
    def __init__(self, nome):
        self.nome = nome 
    def comendo(self, alimento):
        return f'o {self.nome} está comendo {alimento}'
    def executa(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)
leao = Animal('leao')
print(leao.executa('uma gazela'))