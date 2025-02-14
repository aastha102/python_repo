def func(f, x):
    return f(x) # return square(5)

def square(x):
    return x*x

res=func(square, 5)
print(res)

# here f is square , x is 5
# execution starts from line no.7 calling of function - func(square, 5)
# then it will go to line no. 1 func(square, 5)-> which returns square(5) means calling square function
# then go to square(5)-> which return 25
# back to line no. 7
# res=25 coz functions return 25 at last

# Decorator


def outer_func(f):

    def inner_func():
        f() # f means ordinary()
        print("This is nested function")
    return inner_func

@outer_func
def ordinary():
    print("Normal")

print(ordinary())

# Most important powerful feature of python is everything is an object, including functions.

# first class object

def fun1():
    print('Inside fun1()')

fun1() # inside fun1
print(fun1) # address
fun2=fun1 # fun1 and fun2 are pointing to the same object
fun2() # inside fun1
print(fun2) # address

# Passing function as an argument
def alpha(ref): # ref is beta
    print('Inside alpha()')
    ref() # beta()

def beta():
    print("Inside beta()")

alpha(beta) # 1st it will be execute then beta passed as argument, which is equal to ref, 
# ref and beta are pointing to same object then call ref() means beta() inside alpha()

# Function be passed as output from another function
def get_sum(lst):
    print(sum(lst))

def get_product(lst):
    p=1
    for i in lst:
        p *=i
    print(p)

def fun(choice):
    if choice=='sum':
        return get_sum
    else:
        return get_product
    
choice=input("enter your choice") # choice is sum choosen by user
fun1=fun(choice) # fun1 getsum
fun1([10,20,30,40]) # getsum([10, 20, 30, 40])
fun2=fun('product')  # fun2=getproduct
fun2([10,20,30,40]) # getproduct([10, 20, 30, 40])

# Calling an inner function 
# 1st way
def outer():
    print('Inside outer()')

    def inner():
        print('Inside inner()')
    inner()

# 2nd way
def outer():
    print('Inside outer')

    def inner():
        print('Inside inner()')
    
    return inner

in_ref=outer() # execution starts from left side calling outer() 
# in_ref=inner
in_ref() # inner()

# if 0 is present in list it shouldn't be calculated without modifying get_product()
def outer(ref):

    def wrapper(lst):
        if 0 in lst:
            print('o is present')
        else:
            ref(lst) # get_product()
    return wrapper

def get_product(lst):
    p=1
    for i in lst:
        p*=i
    print(p)

mod_get_product=outer(get_product) # mod_get_product=wrapper
mod_get_product([10, 20, 30, 40]) # wrapper([10, 20, 30, 40])
# mod_get_product([10, 0, 40])

# Decorators in python
# It allows programmers to modify the behaviour of function or class.
# It allows us to wrap another functions in order  to extend the behaviour of wrapped function, without permanently modifying it.

def outer(ref): # ref is get_product # def outer(get_product)

    def wrapper(lst): # [10, 20, 30, 40]
        if 0 in lst:
            print('o is present')
        else:
            ref(lst) # get_product(lst)
    return wrapper # none

@outer # decorator
def get_product(lst): # when we have any decorator abovefunction we have to first execute decorator and passed that function as an argument to that decorator.
    # lst or argument passed in inner function
    p=1
    for i in lst:
        p*=i
    print(p)

get_product([10, 20,30]) # it will go to line no. 135 body of get_product()
get_product([10, 0, 30])

# Example2

def outer(ref): # ref is div

    def wrapper(a, b): # 10, 2
        if b==0:
            print('Please provide a non zero denominator')
        else:
            ref(a, b) # div(a, b)
    return wrapper

@outer # name of function 
def div(a, b):
    print(a/b)

print(div(10, 2))
# div(10,0)
div(20, 30)
