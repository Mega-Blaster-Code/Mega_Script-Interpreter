from functions import VirtualMachine
vm = VirtualMachine()


instructions = [""] * 255


def add(instruction):
    for index, inst in enumerate(instructions):
        if inst == '':
            instructions[index] = instruction
            break

#put your code here

# Main loop that processes instructions
while not vm.halted:
    if vm.line >= len(instructions) or instructions[vm.line] == '':
        vm.halt()  # Stop if we reach the end of instructions or an empty line
    else:
        vm.execute_instruction(instructions[vm.line])
        vm.next_line()
