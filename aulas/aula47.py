# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path
# import sys

#de/da     #pasta                 #arquivo
from exer_log_d_programacao import exer10
# import aula45

# valor_de_outra_aula = aula45
# print(valor_de_outra_aula.divide(8,'2'))
exer10.jogo()

# print('Este módulo se chama', __name__)
# print(*sys.path, sep='\n')