# functions.py
import time
class funcoes:
    def __init__(self):
        self.lst = [None for _ in range(255)]
        self.line = int(0)

    def find_var(self, name):
        for i in range(len(self.lst)):
            if self.lst[i] is not None and self.lst[i][0] == name:
                return i
        for i in range(len(self.lst)):
            if self.lst[i] is None:
                return i
        return -1

    def define(self, name, val):
        index = self.find_var(name)
        if index == -1:
            print(f"Sem espaço para definir a variável '{name}'.")
            return
        try:
            val = int(val)
        except ValueError:
            print(f"Valor '{val}' não é numérico e não pode ser definido.")
            return
        self.lst[index] = (name, val)

    def ALU(self, var1, var2, var3, operation):
        index_var1 = self.find_var(var1)
        index_var2 = self.find_var(var2)
        index_var3 = self.find_var(var3)

        if index_var1 == -1 or self.lst[index_var1] is None:
            print(f"A variável '{var1}' não existe.")
            return
        if index_var2 == -1 or self.lst[index_var2] is None:
            print(f"A variável '{var2}' não existe.")
            return
        if index_var3 == -1 or self.lst[index_var3] is None:
            print(f"A variável '{var3}' não existe.")
            return

        try:
            val1 = self.lst[index_var2][1]
            val2 = self.lst[index_var3][1]

            if operation == "sum":
                result = val1 + val2
            elif operation == "sub":
                result = val1 - val2
            elif operation == "mul":
                result = val1 * val2
            elif operation == "div":
                if val2 != 0:
                    result = val1 // val2
                else:
                    print("Can't divide by zero")
                    return
            self.lst[index_var1] = (var1, result)
        except TypeError:
            print("Os valores das variáveis devem ser numéricos.")

    def prn(self, arg):
        if arg[0] == "'":
            print(arg[1:-1])
        else:
            index = self.find_var(arg)
            if index != -1 and self.lst[index] is not None:
                print(self.lst[index][1])
            else:
                print(f"Variável '{arg}' não encontrada.")
    def goto(self,line):
        self.line = int(line)-1

    def get_arg(self, line):
        if len(line) == 0:
            return None, None, None

        first_char = line[0]
        remaining_line = line[1:]

        if first_char == "$":
            var_type = remaining_line.split('.')[0]
            var_name = remaining_line.split('.')[1].split('=')[0]
            value = remaining_line.split('=')[1]
            self.define(var_name, value)
        elif first_char == "!":
            var_type = remaining_line.split('=')[0]
            var_line = remaining_line.split('=')[1]
            self.goto(var_line)
        elif first_char == "#":
            operation = remaining_line.split(':')[0]
            var1 = remaining_line.split(':')[1].split('=')[0]
            var2 = remaining_line.split('=')[1].split('.')[0]
            var3 = remaining_line.split('.')[1]
            self.ALU(var1, var2, var3, operation)
        elif first_char == "/":
            func_type = remaining_line[1:]
            func_type = func_type.split(".")[0]
            val = remaining_line[4:]
            self.prn(val)
        elif first_char == "z":
            val = remaining_line[1:]
            time.sleep(float(val))
