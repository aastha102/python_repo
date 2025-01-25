# Comments-Reading purpose and better understanding about programs
# denotes Single line comment

'''
Multiple line comment
'''

# [Note : If we assigning multiline ''' ''' to var it will be treated as string otherwise comments.]

str = '''
This is all about python.
python var... .
'''
print(str)

a=2

# Identation is required for proper formating of code and better understanding

# Variable - 
# Different steps of variable- Declaration, defination and initialization in single step
# in java

# int d; # Declaration phase in java
# d=20 # initialization

# Declaration, defination and initialization in a single line

# Different data types

d=2 # 2 is value and assigning to variable d
# type() function is used to identify the datatype of variable
print(d, type(d))
# id is used to identify the memory location of the variable. print memory location
print(id(d))
d=2.2
print(d, type(d))
d=3.4
print(id(d))
print(d, type(d))
d=True
print(d, type(d))
d=20+30j
print(d, type(d))
# Declare string in python- double quotaion, single quotation, tripple qoutation
d="Red"
print(d, type(d))
d='Red'
print(d, type(d))

print("Hii", "Hello", "Bye")
# by default seperate word using space
# we want to give explicityly seperator so we use sep keyword
print("Hii", "Hello", "Bye", sep="-")
print("Hii", "Hello", "Bye", sep=":")
print("Hii", "Hello", "Bye", sep="=")
# end keyword is used to print at the end
print("Hii", "Hello", "Bye", end="-")
print("Hii", "Hello", "Bye") # end meand it will start from next line \n
# combination of end and sep
print("Hii", "Hello", "Bye", sep="-", end='|')

# Operators -

# + - addition, * - multiplication, - - minus, / - division, // - floor division , ** - exponential, && and, || or , = assignment operator
# = -> assignment operator is used to asssign the value into the variable
# == equals to operator # that is for comparison of two value


# Muliple  decalration of variable - all var refering to same memory location
a=b=c=d=30
print(a, b, c, d)

# printing memory location of all variables
print(id(a), id(b), id(c), id(d))

# Multiple assignment 
a, b, c, d=30, 40, 50, 60
# a=30, b=40, c=50, d=60

# printing memory location of all variables
print(a, id(a), b, id(b), id(c), id(d))

# operations -

# //- floor division - it eliminates decimal
# / - division

print("#" * 20)
print(20+30, 40-20, 50/2, 50//2, 49//2, 49/2, 2**3)
# 20 and 30 are operands
# addition is operation

# membership operators

# in , is , not in, is not

print('p' in 'python')  # Check it's present or not # it evaluates as true or false
python='python'
print('o' in python)

print('l' in 'python')



print('she' is 'she')
print('she' is 'She') # false coz it is case sensitive - all letter should be same then only give true output

g=5*4*3*2*1
print(g)

#  not in- when word is not present in sentence or word.
print('in' not in 'python')

# is not- it should not be same.
print('in' is not 'python')


# Type conversions- convert one type of data into another type
# two type of conversion- explicit and implicit

# Str can be convert to int, float
a="20"
print(a, type(a))
print(a*2)
b=int(a) # string to integer conversion
print(b*5)
print(b, type(b))
print("==========================================")
# c=str(b)
print(c)

d=40
# c=str(d)
print(c)

# Example: String can convert to any datatype coz hello can't be convert using ascii
# a="Hello"
# print(a)
# b=int(a)
# print(b)

# input() -> This function is used to take the data from the user
str=input("Enter any number")
print(str, type(str))
# a=int(str)
print("Age is", a)

# Here we are converting string to int data type in the same line
# we are asking age from the user then convert this age to int
print("Enter the age of the user:")
age=int(input("Age:"))
print(age, type(age))


# Program - Voting eligibility of candidates
# Take age from the user, and check if the user is eligible or not for voting

age=int(input("Enter your age")) # Converting string to int
print(type(age))
if age>18:
    print("You are eligible")

age=input("Enter your age") # Converting string to int
age=int(age)
print(type(age))
if age>18:
    print("You are eligible")

