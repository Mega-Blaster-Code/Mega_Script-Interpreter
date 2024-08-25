from functions import *
lst = [None for _ in range(100)]

def define(name, val):
    index = let(name, val, lst)

    if index == -1:
        print(f"Variável '{name}' já existe")
    else:
        print(f"Variável '{name}' inserida no índice {index}")


for i in range(10):
    define(f"x", 25)

print(lst)
