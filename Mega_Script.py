# Mega_Script.py
from functions import FUNC

vm = FUNC()

func_list = ["" for _ in range(255)]


def add(tex):
    for j in range(len(func_list)):
        if func_list[j] == '':
            func_list[j] = tex
            break


halt = False
add("$define.x=0")
add("$define.add=1")
add("#sum:x=x.add")
add("/prn.x")
add("!goto=2")

while not halt:
    if vm.line >= len(func_list) or func_list[vm.line] == '':
        halt = True
    else:
        inst = func_list[vm.line]
        if inst == "halt":
            halt = True
        else:
            vm.get_arg(inst)
        vm.line += 1