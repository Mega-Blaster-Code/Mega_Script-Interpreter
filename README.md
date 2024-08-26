# Mega_Script Interpreter

Mega_Script is a low-level programming language interpreter designed for simplicity and flexibility. This language is still in development and will include a compiler in the future. The interpreter is implemented in Python, consisting of two main files: `Mega_Script.py` and `functions.py`.

## Table of Contents
- [Overview](#overview)
- [Basic Usage](#basic-usage)
- [Language Features](#language-features)
  - [Variable Management](#variable-management)
  - [Arithmetic Operations](#arithmetic-operations)
  - [Jump To](#JumpTo)
  - [Functions](#functions)
  - [Printing](#printing)
  - [Conditional Jumps](#conditional-jumps)
- [Future Work](#future-work)

## Overview
Mega_Script is a low-level language interpreter that allows you to define variables, perform arithmetic operations, control the flow of execution, and create custom functions. The interpreter reads instructions line by line and executes them according to the syntax provided.

## Basic Usage
To use the interpreter, add your instructions to the `func_list` in the `Mega_Script.py` file. Each instruction should be in a specific format, which will be executed sequentially. 

Here’s a simple example:

```python
add("$define.x=0")       # Define a variable x with the value 0
add("$define.add=1")     # Define a variable add with the value 1
add("#sum:x=x.add")      # Sum the values of x and add, store the result in x
add("/prn.x")            # Print the value of x
add("!jumpto=2")           # Go to line 2
```

## Language Features

### Variable Management
- **Definition**: Variables can be defined using the `$define` keyword.
  - `$define.x=0` - Defines a variable `x` with the value `0`.
  - `$define.y=10` - Defines a variable `y` with the value `10`.
  - `$define.z=87` - Defines a variable `z` with the value `87`.

### Arithmetic Operations
- Supported operations are addition, subtraction, multiplication, and division.
  - `#sum:var1=var2.var3` - Adds the value of `var2` to `var3` and stores the result in `var1`.
  - `#sub:var1=var2.var3` - Subtracts the value of `var3` from `var2` and stores the result in `var1`.
  - `#mul:var1=var2.var3` - Multiplies `var3` by `var2` and stores the result in `var1`.
  - `#div:var1=var2.var3` - Divides `var3` by `var2` and stores the result in `var1`.

### JumpTo
- **jumpto**:
  - Jump to a specific line using the `jumpto` keyword.
  - `!jumpto=line` - Jumps to the specified line.

### Printing
- **Print**: Display values or strings using the `prnt` keyword.
  - `prnt.~var` - Prints the value of a variable.
  - `prnt.'string'` - Prints a string.
  - `prnt.++~var` - Converts a number to a character and prints it.
  - `prnt.endl` - Prints a newline.

### Functions (Not Implemented Yet)
- Define and call functions using the `func` keyword.
  - `func.name` - Defines a function named `name`.
  - `func.~name` - Calls the function named `name`.
  - `func.{go}~name` - Jumps to the function without returning.

- **Return**: Use `return` to exit a function.

### Conditional Jumps (Not Implemented Yet)
- **Conditional Jumps**: Compare variables and jump to a specific line if the condition is met.
  - `&if_g:var.var=line` - Jumps if the first variable is greater than the second.
  - `&if_l:var.var=line` - Jumps if the first variable is less than the second.
  - `&if_e:var.var=line` - Jumps if both variables are equal.
  - `&if_d:var.var=line` - Jumps if both variables are not equal.
  - `&if_z:var=line` - Jumps if zero.

## Future Work
- **Compiler Implementation**: In the future, Mega_Script will include a compiler to translate the language into assembly or other low-level languages.
- **Error Handling**: Currently, basic error handling is implemented, but more sophisticated checks and messages will be added.
- **Optimizations**: As the project is still in its initial phase, the program is not fully optimized and requires additional adjustments to improve its performance and functionality.

## Examples

### Example 1: **Infinite Hello World**
This example continuously prints "hello world".

```python
add("/prn.'hello world'")  # Prints 'hello world'
add("!jumpto=0")           # Jumps back to the first line, creating an infinite loop
```

### Example 2: **Basic Addition**
This example demonstrates a simple addition operation between two variables and prints the result.

```python
add("$define.a=7")        # Define a variable a with the value 7
add("$define.b=3")        # Define a variable b with the value 3
add("$define.result=0")   # Define a variable result with the value 0
add("#sum:result=a.b")    # Add num1 and num2, storing the result in 'result'
add("/prn.result")        # Print the result of the addition
```

### Example 3: **Multiplication Example**
This example multiplies two numbers and prints the result.

```python
add("$define.a=5")           # Define a variable a with the value 5
add("$define.b=10")          # Define a variable b with the value 10
add("$define.result=0")      # Define a variable result with the value 0
add("#mul:result=a.b")       # Multiply a and b, storing the result in 'result'
add("/prn.result")           # Print the result of the multiplication
```


### Example 4: **Simple Counter**
This example increments a counter and prints its value.

```python
add("$define.counter=0")    # Define a variable counter with the value 0
add("$define.increment=1")  # Define a variable increment with the value 1
add("#sum:counter=counter.increment") # Increment the counter by 1
add("/prn.counter")         # Print the current value of counter
add("!jumpto=2")            # Jump back to the third line to repeat the process
```


