# def contagem():
#     num = 0
#     for _ in range(10):
#         num +=2
#         print(num)
# contagem()
def conta(num, num2):
    return num % num2 == 0
resultado_conta = conta(16, 8)
print(resultado_conta)