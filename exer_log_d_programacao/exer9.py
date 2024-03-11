'''
Contagem de Vogais e Consoantes:
Crie um programa que conte o número de vogais e consoantes
em uma palavra ou frase inserida pelo usuário.
Considere apenas letras do alfabeto 
(ignorando espaços, números e caracteres especiais).'''

palavra = 'onibus'
vogais = 'aeiou'
consoantes = len(palavra)
tem_vogal = any(vogal in palavra for vogal in vogais)
if tem_vogal:
    print(tem_vogal, consoantes)
else:
    print(False)