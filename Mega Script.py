from functions import *
lst = [None for _ in range(255)]

def define(name, val):
    index = find_var(name, lst)
    if index == -1:
        print(f"Sem espaço para definir a variável '{name}'.")
        return
    lst[index] = (name, val)

def sum(var1, var2, var3):
    index_var1 = find_var(var1, lst)
    index_var2 = find_var(var2, lst)
    index_var3 = find_var(var3, lst)

    if index_var1 == -1 or lst[index_var1] is None:
        print(f"A variável '{var1}' não existe.")
        return
    if index_var2 == -1 or lst[index_var2] is None:
        print(f"A variável '{var2}' não existe.")
        return
    if index_var3 == -1 or lst[index_var3] is None:
        print(f"A variável '{var3}' não existe.")
        return
    lst[index_var1] = (var1, lst[index_var2][1] + lst[index_var3][1])

define("x",5)
define("y",10)
define("z",5)
print(lst)
sum("x","y","z")
