def soma(x ,y, /, *args):
    return x + y + sum(args)
print(soma(1,2,5,5,8,5,2))