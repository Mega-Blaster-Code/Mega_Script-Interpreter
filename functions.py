import time

class VirtualMachine:
    def __init__(self):
        self.variables = {}
        self.line = 0
        self.halted = False

    def halt(self):
        self.halted = True

    def define_variable(self, name, value):
        # Define a variable with a name and value
        try:
            value = int(value)
        except ValueError:
            print(f"Value '{value}' is not numeric and cannot be defined.")
            return
        self.variables[name] = value

    def perform_alu_operation(self, var1, var2, var3, operation):
        # Perform arithmetic operations on variables
        if var1 not in self.variables:
            print(f"Variable '{var1}' does not exist.")
            return
        if var2 not in self.variables:
            print(f"Variable '{var2}' does not exist.")
            return
        if var3 not in self.variables:
            print(f"Variable '{var3}' does not exist.")
            return

        val2 = self.variables[var2]
        val3 = self.variables[var3]

        if operation == "sum":
            result = val2 + val3
        elif operation == "sub":
            result = val2 - val3
        elif operation == "mul":
            result = val2 * val3
        elif operation == "div":
            if val3 != 0:
                result = val2 // val3
            else:
                print("Cannot divide by zero.")
                return
        else:
            print(f"Unknown operation '{operation}'")
            return

        self.variables[var1] = result

    def print_variable_or_text(self, arg):
        # Print a variable value or a string
        if arg.startswith("'"):
            print(arg[1:-1])
        elif arg in self.variables:
            print(self.variables[arg])
        else:
            print(f"Variable '{arg}' not found.")

    def goto_line(self, line_number):
        # Jump to a specific line number
        self.line = int(line_number) - 1

    def execute_instruction(self, instruction):
        # Process an instruction based on its first character
        if not instruction:
            return

        first_char = instruction[0]
        remaining_instruction = instruction[1:]

        if first_char == "$":
            # Handle variable definition
            var_type = remaining_instruction.split('.')[0]
            if var_type == "define":
                var_name = remaining_instruction.split('.')[1].split('=')[0]
                value = remaining_instruction.split('=')[1]
                self.define_variable(var_name, value)

        elif first_char == "!":
            # Handle goto instruction
            var_type = remaining_instruction.split('=')[0]
            if var_type == "jumpto":
                line_num = remaining_instruction.split('=')[1]
                self.goto_line(line_num)

        elif first_char == "#":
            # Handle arithmetic operations
            operation = remaining_instruction.split(':')[0]
            var1 = remaining_instruction.split(':')[1].split('=')[0]
            var2 = remaining_instruction.split('=')[1].split('.')[0]
            var3 = remaining_instruction.split('.')[1]
            self.perform_alu_operation(var1, var2, var3, operation)

        elif first_char == "/":
            # Handle print operation
            func_type = remaining_instruction.split(".")[0]
            if func_type == "prn":
                val = remaining_instruction[4:]
                self.print_variable_or_text(val)

        elif first_char == "z":
            # Handle sleep operation (delay)
            val = remaining_instruction[1:]
            time.sleep(float(val))

    def next_line(self):
        # Move to the next line in the script
        self.line += 1
