# Conditional Statements/Decision Making stements in Python

# Conditional statements in Python are used to execute certain blocks of code based on specific conditions. 
# These statements help control the flow of a program, making it behave differently in different situations.
# It is the simplest form of a conditional statement. It executes a block of code if the given condition is true.

# Syntax -

# if condition:
    # Statements to execute if
    # condition is true

age=9 # declaring of variable
# it will execute the condition if the evaluated condition is true
# if the condition is false, it will do nothing
# proper is required so compiler know that it is block of if statement
if age>18:
    print("You are eligible")

# Short Hand if
# Short-hand if statement allows us to write a single-line if statement.

# Syntax:
# if condition: statement
if age>18: print("You are eligible")

# if else Conditional Statements in Python
# It allows us to specify a block of code that will execute if the condition(s) associated with an if or elif statement evaluates to False. Else block provides a way to handle all other cases that don't meet the specified conditions.

# if condition is ture, iif block executes otherwise else block will executes

# Syntax of if-else: 
# if condition:
    # code to execute if condition is true

# else:
    # code to execute if condition is false

if age>18:
 print("You are eligible")
else:
    print("You are not eligible")


# short Hand if-else
# The short-hand if-else statement allows you to write a single-line if-else statement.
# Note: This method is also known as ternary operator. Ternary Operator essentially a shorthand for the if-else statement that allows us to write more compact and readable code, especially for simple conditions.


# Syntax:

# statement_if_true if condition else statement_if_false
print("You are eligible") if age>20 else print("You are not eligible")

# elif Statement
# elif statement in Python stands for "else if." It allows us to check multiple conditions , providing a way to execute different blocks of code based on which condition is true. Using elif statements makes our code more readable and efficient by eliminating the need for multiple nested if statements.

# Syntax:
# if condition1:

#     # code to execute if condition1 is true

# elif condition2:

#     # code to execute if condition2 is true

# else:

    # code to execute if none of the above conditions are true
 
# # If converting data from str to int or float it must be stored to some variable
# age=int(input("Enter your age"))

# if age>20 and age<100: # Checking age from 21 to 99 
#    print("You are eligible")
# elif age<=20: # we are checking age from 1 to 20 includes 20 also
#    print("You are not eligible")
# else:
#    print("You are not part of it")


# #[Note: For indentation- The number of spaces is up to you as a programmer, the most common use is four, but it has to be at least one.]
# # It should same number of spaces in the same block of code, otherwise Python will give you an error:

# # Example
# # Syntax Error:

# # if 5 > 2:
# #  print("Five is greater than two!")
# #         print("Five is greater than two!")

# # age=int(input("Enter your age"))
# # print(type(age))
# name=input("Enter your name")
# print(type(name))
# if age>=18:
#    if name == "Vijay":
#       print("You are eligible")
#    else:
#       print("Sorry!! you are not")
# else:
#    print("You have wrong output")

# if age>=18 and name=="Vijay":
#       print("You are eligible")   
# else:
#    print("You have wrong output")

# Play rules
# if the age group is 1 to 10- You can take ludo, chess
# 10-20- basket ball, volleyball
# 20- 30 - anygame
# if exceeds 30- you are not eligible

school_name=input("enter your school name")   
age=int(input("enter your age:"))

# checking if school name is  kv then enter into if block , if the school name is something else then just execute else block

if school_name=="kv": # if yopu have kv means you can enter inside it. " # 18 == kv 
    # 121 to 127 is the part of line no. 120 if block 
    # if the line no. 120 condition is false then it will not enter into this block
    if age<=10:
        print("you can take ludo,chess")
    elif age>10 and age<20:
        print("you can take basket ball")
    else:
        print("none")
# else:
#     print("you are not a part of school")
else:
    pass # it means nothing

# ask school name from user and if school_name is kv then ask age from user and then do futher operation if school_name is something else - you are not part of school







# Nested if..else Conditional Statements
# Nested if..else means an if-else statement inside another if statement. We can use nested if statements to check conditions within conditions.