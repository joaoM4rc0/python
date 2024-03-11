"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os
palavra_secreta = 'televisao'
letra_certa = ''
numero_tentativas = 0
while True:
    letra_digitada_usu = input('digite uma letra: ')
    numero_tentativas +=1 
    if len(letra_digitada_usu) > 1:
         print('voce só pode digitar uma letra!')
         continue
    
    if letra_digitada_usu in palavra_secreta:
        letra_certa += letra_digitada_usu 

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letra_certa:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print('palavra formada: ', palavra_formada)
    if palavra_formada == palavra_secreta:
            os.system('cls')
            print('VOCE GANHOU!')
            print('A palavra era', palavra_secreta)
            print('Tentativas:', numero_tentativas)
            letras_acertadas = ''
            numero_tentativas = 0

