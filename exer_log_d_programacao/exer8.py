'''
Verificação de Palíndromos:
Escreva um programa que verifique se uma palavra
ou frase é um palíndromo
. Um palíndromo é uma palavra, 
frase ou sequência de caracteres que permanece a mesma
 quando lida de trás para frente (desconsiderando espaços e pontuação).
Exemplo: “arara” é um palíndromo.'''

palavra = 'cachorro' 

palavra_invertida = palavra[::-1]
if palavra == palavra_invertida:
    print(True) 
else: 
    print(False)