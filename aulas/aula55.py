import pymysql
def recursiva(x):
    if x ==1:
        return x
    
    return x * recursiva(x - 1)
print(recursiva(5))
