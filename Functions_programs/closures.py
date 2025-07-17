# A closure is a function defined inside another function that remembers the variables from the outer (enclosing) 
# function even after the outer function has finished execution.
'''
Closure = Function + Free Variables (Remembered)
It allows the inner function to capture and use variables from the enclosing scope without using global or nonlocal explicitly.
'''

def outer():
    x = 10         

    def inner():
        print("x", x)     

    return inner

inner=outer()#inner
print(inner())

# x is not defined inside inner, but it’s still accessible.
# inner closes over x → That's a closure.


def logger(prefix):
    def log(message):
        print(f"{prefix}: {message}")
    return log

error_logger = logger("[ERROR]")
info_logger = logger("[INFO]")

error_logger("Something went wrong")
info_logger("System started")

