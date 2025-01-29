# Python Functions

# without input without output

def mul(): # defination of the function
    a=10 # line 6 to 8 body/statements of the function
    b=20
    print(a*b)

mul() # Calling of function

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
toppings_t("cheese", "butter", "miyonees")

def topping_p(*tpng, chrust):
    print(tpng)
# topping_p("cheese", "butter", "miyonees") # topping_p() missing 1 required keyword-only argument: 'chrust'
topping_p("cheese", "butter", "miyonees",chrust="water") # we have to use keyword to pass value to chrust or defult.

def topping_p(*tpng, chrust="water"): 
    print(tpng)
topping_p("cheese", "butter", "miyonees") # no error coz default argument is used.

# [Note: Either keyword or default argument used when we use 2nd parameter in function defination with variable length arguments.]


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
    return a*b
c=mul_c() # store the value which is return from function to var c.
print(mul_c()) # Print the return value frrom function directly.
print(c)

# with input with output- We are passing value to function, then function returns the output.
def expo_c(a,b):
    return a**b

c=expo_c(2,3) # store the output to var c
print(c)




