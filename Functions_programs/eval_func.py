# The eval() function in Python is used to evaluate a string as a Python expression and return the result.
# Syntax: eval(expression, globals=None, locals=None)

'''
expression: A string that represents a valid Python expression.
globals (optional): A dictionary to specify the global namespace.
locals (optional): A dictionary to specify the local namespace.

'''
# example 1
x = 10
print(eval('x + 5'))   # Output: 15

# example 2
y=[10, 20, 30]
print(eval("y"))

# example 3
age=input("Enter your age")
print(eval('int(age)*5'))

# example 4
def square(x): return x*x
def cube(x): return x*x*x

fn_name = input("Enter function name (square/cube): ")
n = int(input("Enter number: "))
print(eval(f"{fn_name}({n})"))

# example 5
def power(x, y):
    return x ** y

expr = "power(a, b)"
print(eval(expr, {"power": power, "a": 2, "b": 3}))  # Output: 8

# example 6
def calculator():
    while True:
        expr = input("Enter expression (or 'q' to quit): ") # 20+30, 20*50
        if expr.lower() == 'q':
            break
        try:
            print("Result:", eval(expr))
        except Exception as e:
            print("Invalid expression:", e)

calculator()

# example 7

def add(x, y): return x + y
def sub(x, y): return x - y

operation = input("Enter operation (add or sub): ")  # e.g. "add(10, 5)"
print("Result:", eval(operation))  # Output: 15







