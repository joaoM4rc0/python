def saudacao(msg):
    return msg

def executa(funcao, msg):
     return funcao(msg)
funcao_executada = executa(saudacao, 'neymar é melhor que messi')
print(funcao_executada)

