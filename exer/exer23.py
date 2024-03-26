# Exercício - Salve sua classe em JSON
# e depois crie novamente as instâncias
# Salve os dados da sua classe em JSON
# da classe com os dados salvos
# Faça em arquivos separados.
import json
CAMINHO_ARQUIVO = 'exer23_b.json'
class Pessoa :
    ano_atual = 2024
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def ano_nascimento_pessoa(self):
        ano_nascimento = self.ano_atual - self.idade

        
p1 = Pessoa('joao', 19)
ano_nascimento = p1.ano_nascimento_pessoa()
p2 = Pessoa('joana', 39, )
p3 = Pessoa('cristiano',29)

dados = [vars(p1), p2.__dict__, p3.__dict__]

def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
        json.dump(
            dados,
            arquivo,
            indent= 2 ,
            ensure_ascii=False,
        )
if __name__ == '__main__':
    fazer_dump()