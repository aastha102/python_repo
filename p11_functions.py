from functools import reduce

# Python Functions - Reusable piece of component / Reusability

# We can call/invoke function only after the declaration of function.
# declare function using def 
# def mul(defination):
#     Body of function
# mul() # calling of function # outside of function

# without input without output

def mul(): # defination of the function
    a=10 # line 6 to 8 body/statements of the function
    b=20
    print(a*b)

print(mul()) # None # Calling of function 
# If we print userdefined function inside print statement, will get output if function returns value will get that value, or else by default None
mul()
result=mul() # None value get stored to result var

# With input without output

# Positional arguments -

def mul(a, b):
    print(a*b)
mul(3, 4) # Here the arguments are 3, 4 and parameters are a, b where a gets assigned as 3 and b gets assigned as 4 based on the positions.
mul(5, 2) # Here the arguments are 5, 2 and parameters are a, b where a gets assigned as 5 and b gets assigned as 2 based on the positions.
# mul(2) # Error - Here one argument is missing.
# [Note: In poisitional arguments, aguments must be same as parameters.]

# Default arguments -

def expo(a, b=9):
    print(a*b)
expo(5, 2) # Here the arguments are 5, 2 and parameters are a, b where a gets assigned as 5 and b gets assigned as 2, 2 replaced with 9 based on the positions.
expo(2)# Here a value is 2 , b has default value 9, if not passing anything means use default value.
# [Note: In default argument, if default value assigned to parament in function itself, passing value through function is optional.
#  If we pass it will use that value otherwise default value,]
def add(a=10, b=20):
    print(a+b)
add() # here if we don't pass anything won't throw any error coz used default arguments assigned to parameters.
# def mul_d(a, b=90, c): 
# [Note: Non default agrument can't follow default argument, after using default agumrnt, cannot use non default agument.]
# Default argument be at last
def mul_d(a, b, v=90):
    print(a*b+v)# No error default used at last

# Keyword arguments

# In positional arguments we noticed that if order changes the output also changes. We can overcome this by using keyword arguments. 

def power_of(x, y):
    print(x+y)
power_of(y=20, x=30) # here we are using keyword so if we interchange the position, values will not change.


# Variable length arguments

# Passing any number of arguments to a function is called as variable length argument.

def toppings(tpng):
    print(tpng)
toppings("miyonees")
# toppings("cheese", "butter") # Error toppings() takes 1 positional argument but 2 were given

# By attaching a star or asterisk in front of the parameter, the function is now ready to take different number of arguments.
# This is because toppings is now considered as tuple.
def toppings_t(*tpng):
    print(tpng, type(tpng)) 
    print(len(tpng))
toppings_t("cheese", "butter", "miyonees")

def topping_p(*tpng, chrust):
    print(tpng)
# topping_p("cheese", "butter", "miyonees") # topping_p() missing 1 required keyword-only argument: 'chrust'
topping_p("cheese", "butter", "miyonees", chrust="water") # we have to use keyword to pass value to chrust or defult.

def topping_p(*tpng, chrust="water"): 
    print(tpng)
topping_p("cheese", "butter", "miyonees") # no error coz default argument is used.

def topping_o(*tpng, water):
    print(tpng)
    print(water, len(water))
topping_o("Air", " bottle", water="Liquid") # calling topping_o function
topping_p("Air", " bottle", chrust="Liquid") # calling topping_o function
# topping_p("Air", " bottle", water="Liquid") # error- coz no paramter water is used in function defination of topping_p

# [Note: Either keyword or default argument used when we use 2nd parameter in function defination with variable length arguments.
# Variable length argument must be last parameter, while passing keyword argument it must be at last]


# Variable keyword length arguments

# Passing dictionary to function.

def goal(**rec):
    print(rec)
goal(name="ria", age=20, sal=20000)
# def goal_m(member, **rec_c, mt) # we can only use paramter before VKL, after this we can't use any parameter. 

def goal_c(member, **rec_c): 
    print("Member is ", member)
goal_c(name="ria", age=20, sal=20000, member=20)

# without input with output- We don't pass the value to function but function returns the output.
def mul_c():
    a=10
    b=20
    c=a*b 
    print(c)
    return c # function can return only one value i.e output/result. 
 # If we are returning multiple value so it will considered as tuple
    
# c=mul_c() # store the value which is return from function to var c.
# print(mul_c()) # Print the return value frrom function directly.
# print(c)
mul_c()
print(mul_c())  # after operation of function completes , 200 in place of mul_c -> print(200)
op=mul_c() # 200 returns as output from function then, we are storing 200 to op
print(op)

kt=mul_c()
print(mul_c(), kt)

print()

# with input with output- We are passing value to function, then function returns the output.
def expo_c(a,b):
    print("With input with output")
    return a**b

c=expo_c(2,3) # store the output to var c
# print(c)
print(c, expo_c(3,4), expo_c(7,2), c*10)
# execution of line no. 136- first 134 executes then print(c, 8, 49, 80) before printing this it will executes body of the function
# Body of the function it executes whenever we call the function.
print("Apple", expo_c(4, 5), expo_c(2, 2), c)

''' ------------------------------------------------------------------------------------------------------------------------------ '''

# Lambda Function

# lambda function is anonymous function (nameless function)
# no need to give name of function
# it's like a anonymous class in java

# For using lamba function, give a name to lambda function
mul_l=lambda num, p:num*p
print(mul_l(4,2))
print(mul_l(9,2))

 # single line function same line calling which accepts parameter 
 # temperory use function
res=(lambda num,p:num*p)(3,2)
print(res)

# General use of lamba

# filter() - The filter() method filters the given sequence.
#  With the help of a function that tests each element in the sequence to be true or not.

lst=[10,30,35,65,40,50]

def fun(x):
    if x%2==0:
        return True
    else:
        return False
print(list(filter(fun, lst)))

# using lambda with filter function
# filtering out all 
print(list(filter(lambda x: x%2==0, lst))) # convert it into list.

# reduce() it is present inside module functools

def fun(x,y):
    return x+y
print(reduce(fun, lst)) 
# It gives addition of element

#Using lambda function with reduce function
print(reduce(lambda x,y:x+y, lst))# we are not type casting coz it gives single value

# map() - Perform any operation on list.

def fun(x):
    return x**2

print(list(map(fun, lst)))

# using lambda function
print(list(map(lambda x:x**2, lst)))

# return lambda function into one function
def func1(num):
    return lambda x: x*num
# print(func1(2)(5)) # 2 is argument for func1 and (5) is calling lambda function
func2=func1(2) # num =2
print(func2(5)) # x=3

def func3(num):
    return lambda x:x*num
print("Enter a number which table you want to print")
x=int(input())
fun4=func3(x) # storing return statement of lambda function
for i in range(1,10):
    print(fun4(i)) # i assigned to num var
    print(x, "*", i,"=",fun4(i))

'''--------------------------------------------------------------------------------------------------------------------------------'''

# Return Keyword

# Function can return multiple values, but it will store inside tuple.

def func():
    a=20
    b=30
    c=40
    return a, b, c
res=func()
print(res) # tuple will get as output
# r1, r2, r3= func() # no. of variables equals to no. of return variables

# unpacking of tuple
r1, r2, r3=res 
print(r1, r2)

'''--------------------------------------------------------------------------------------------------------------------------------'''

# if __name__== '__main__':
#     main()
#  it will check main function if it is present then it will execute function from import module which is called under main()
#   





