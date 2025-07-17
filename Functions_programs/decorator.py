# A decorator in Python is a special function that modifies the behavior of another function or class without changing its source code. 
# Decorators are often used to add reusable functionality, such as logging, timing, or access control.

# How it works:
# A decorator takes a function as input and returns a new function.
# You apply a decorator using the @decorator_name syntax above a function definition.

# Example
def print_args(func): # multiply
    def wrapper(*args, **kwargs): 
        print(f"Arguments: {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@print_args
def multiply(a, b):
    return a * b

print(multiply(2, 3))

# Example of a simple decorator that logs the start and end of a function execution
def log_decorator(func):
    def wrapper():
        print("Starting...")
        func()
        print("Finished.")
    return wrapper

@log_decorator
def say_hi():
    print("Hi!")

say_hi()

# Example of a decorator that modifies the output of a function
def square_output(func):
    # Decorator that returns the square of the result
    def wrapper(a, b):
        return func(a,b)

    return wrapper

@square_output
def add(a, b):
    return a + b

print(add(2, 3))  # Output: 25

# Square the Output
def outer(func):
    def wrapper(a, b):
        result=func(a, b)
        return result**2
    return wrapper

@outer
def sqr(a, b):
    return a+b

print(sqr(2,5))

# No. of times function
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello {name}")

greet("Vijay")

# Multiple decorator
def decor1(func):
    def inner():
        return func().upper() # full_name.split()
    return inner

def decor2(func):
    def inner():
        return func().split() # full_name.split()
    
    return inner

@decor2
@decor1
def get_name():
    name=input("Enter first name")
    last_name=input("Enter last name")
    return name + " " + last_name

print(get_name())


greet("Vijay")

# Multiple decorator with repetation
def decor1(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.title()  # For better name formatting
    return inner

def decor2(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.split()  # Split into [first, last]
    return inner

def repeat(n):
    def decor_repeat(func):
        def inner(*args, **kwargs):
            results = []
            for _ in range(n):
                results.append(func(*args, **kwargs))
            return results
        return inner
    return decor_repeat

@repeat(2)
@decor2
@decor1
def get_name():
    name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    return name + " " + last_name

print(get_name())


