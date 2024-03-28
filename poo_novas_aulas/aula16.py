from abc import ABC, abstractmethod

class minhaclasseabstrata(ABC):
    @abstractmethod
    def metodo_abstrato(self):...
class minhaclassefilha(minhaclasseabstrata):
    def metodo_abstrato(self):
        print('olá mundo')
classe = minhaclassefilha()
classe.metodo_abstrato()