# Namespace Type	When Created	                        Scope
# Built-in	        When Python interpreter starts	        Accessible everywhere
# Global	        When a module is loaded	                Entire module
# Enclosing	        For outer functions (in nested defs)	Outer function only
# Local	            When a function is called	            Inside the current function

# 1. Built-in Namespace
# Contains all the built-in functions and exceptions (e.g., len, int, Exception)
# Created when the Python interpreter starts

#  2. Global Namespace
# Created when a Python file (module) is run
# Contains global variables, functions, classes, etc.
# Exists until the script ends

#  3. Enclosing Namespace (Nonlocal)
# Applies to nested functions
# The outer function's local variables form the enclosing namespace for the inner function

# 4. Local Namespace
# Created inside a function when it's called
# Stores function arguments and local variables

'''
Scope Resolution — LEGB Rule
When Python looks for a variable, it checks in this order:

L → Local
E → Enclosing
G → Global
B → Built-in
'''

x = "global"
def outer():
    x = "enclosing"
    y=20
    def inner():
        nonlocal y
        x = "local"
        y=y+5 # UnboundLocalError: local variable 'y' referenced before assignment
        print(y)
        print(x)  # Output: local
    inner()
    print(x)
outer()
print(x)
