# A partial function is a new version of an existing function with some arguments fixed (pre-filled) using functools.partial.
# It’s useful when you want to simplify function calls or reuse a function with default values for certain arguments.

#[ Recommended to use keyword argument]

# Create a partial function that always multiplies by 2
from functools import partial
def multiply(x, y):
    return x*y

# mulitply(10,20)
mul=partial(multiply,x=2) # multiply 2, y=5 i.e x is fixed coz bydefault it takes 1st one if it is positional argument
# print(mul(y=5)) 
# # print(mul(3,5)) # multiple value for x
# print(mul(3)) # x=3, no values for y
# # print(mul(x=4)) # Error coz x is already fixed and overiding x and no value for y
print(mul(y=5))
# print(mul(x=7, y=5)) # Muliple value for x

# partial functtion using function
def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
print(square(4))
# print(square(2, 3))
print(square(base=8, exponent=8))

# partial function using lambda 
sqr=(partial((lambda base, expo:base**expo), expo=3))(base=7)
print(sqr)

# # partial functtion using function
# def format_message(prefix, message, suffix):
#     return f"{prefix} {message} {suffix}"

# error_msg = partial(format_message, prefix="[ERROR]", suffix="!!")
# print(error_msg("File not found"))

# partial function using lambda 
err_mg=(partial((lambda pref,msg,suff:f"{pref}{msg}{suff}"),pref="[ERROR]", suff="!!"))(pref="Wrong",msg="Not Found")
print(err_mg) 
#[Note-if we are using keyword argument Should use keyword in call as well. 
# Never pass the same argument both positionally in partial() and then again via keyword when calling — it leads to TypeError.]

multiply=partial((lambda x,y:x*y),x=2) # Erroe can not override positional argument
print(multiply(x=3, y=5))

# Partial Function-
# create a new function with one or more arguments pre-supplied.
# The original function remains unchanged.
# Very useful in functional programming and callback scenarios.

'''
Feature	             Default Argument	                        Partial Function
Declared in	         Function definition	                    Created using functools.partial()
When used	         At call time if argument not passed	    At function creation time
Customization	     Per call basis	                            Pre-fixed for reuse
Flexibility	         Only for parameters	                    Can fix args, kwargs, and work with any callable
Example use case	 print(msg="Hi")	                        partial(func, arg1=...) for callbacks, APIs

'''

# Default Arguments-
# Default arguments are defined at function declaration time.
# The value is used only if the caller doesn’t provide it.
# Works only with function parameters, not fixed values elsewhere.