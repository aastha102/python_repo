# Lambda Function Use Case

from functools import reduce
lst=list(range(21))
print(lst)

def func_list():
    even_lst=[] # even list
    for i in lst:
        if i%2==0:
            even_lst.append(i)
    return even_lst
print(func_list())

def fun(x):
    if x%2==0:
        return True
    else:
        return False
print(list(filter(fun, lst)))
print(fun(21))

even_lst=list(filter(lambda x: x%2==0, lst))
print(even_lst)
odd_lst=list(filter(lambda n : n%2!= 0, lst))
print(odd_lst)
print(reduce(lambda x,y: x+y, lst))
[1, 2, 3, 4, 5, 6]
sum=0
for i in range(1, 5):
    sum=sum+i # x+y
    # 1st step sum= 0+1 =1
    # 2nd step sum=1 + 2=3
    # 3rd step sum=3+3=6
    # 4th step sum=6+4=10


def square_list(lst):
    global numbers
    return[num**2 for  num in lst]
numbers=[1,2,3,4]
print(numbers)
# squared_number =square_list(numbers)
print("square_list:",square_list(numbers))



'''---------------------------------------------------------------------------------------------------------------------------------'''

# Scope of Variable

# Global variable - can be accessible outside of function or inside of function, Accessible for all.
# Local variable - It can be accessible inside that function where it is declared.

def fun3():
    y=30 # local variable
    print(y) # accessible after calling of function
# print(y) # Not sccessible coz it is outside of function

x=20 # global variable
def fun(x):
    global y # global varaible declaring inside function using keyword global
    y=20 # local variable
    print(x, y)
fun(x)
print(x, y) # We can print global variable which declared inside function.
fun(y) # we can pass global varible to that function wehre that global var is declared.

# def fun1(y):
#     global y # error y is assigned before global declaration of y coz y is used as parameters in fun1
#     y=30
# To resolve above problem - name of parameter should be different from global variable name


