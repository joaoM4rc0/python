for i in range(10):
    if i == 2:
        print('o 2 foi encontrado')
        continue
    if i == 5:
        print('o 8 foi encontrado, encerrando o laço ...')
        break
    for j in range(8, 15): 
        print(i, j)
else: 
    print('nenhum número foi encontrado')