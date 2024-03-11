'''Jogo da Adivinhação:
Implemente um jogo de adivinhação
em que o computador escolhe um número aleatório entre 1 e 100,
e o usuário tenta adivinhar qual é esse número.
Dê dicas ao usuário se o número é maior ou menor 
do que a tentativa anterior.
'''
import random
def jogo():
    numero_aleatorio = random.randint(1,100)
    def numero_escolhido_usu():
        tentativas = 0
        while True:
            numero_usu = input('digite um número: ')
            int_numero_usu = int(numero_usu)
            if int_numero_usu == numero_aleatorio:
                print('Parabens voce acertou o número')
                break
            else:
                tentativas +=1
                if numero_aleatorio > int_numero_usu:
                    print(f'o numero é maior que {int_numero_usu}')
                else: 
                    print(f'o numero é menor que {int_numero_usu}')
        print(f'{tentativas= }')
        return numero_usu
    return numero_escolhido_usu()
jogo()