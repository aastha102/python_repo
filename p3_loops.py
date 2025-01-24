# Iterator / Looping Statement

# while, for and nested Loops

# while Loop-
# a while loop is used to execute a block of statements repeatedly until a given condition is satisfied. 
# When the condition becomes false, the line immediately after the loop in the program is executed.

# Syntax - 
# while expression/condition:
#     statement(s)

# For any repetetive task- we require looping
# 

# Program to print number from 1 to 100
i=1 # this will execute only 1 time at the time of initialization.
# line no. 22 to 24 process goes till the condition is false
# if condition is false then immidiatally it will terminate loop

# here value is 1
while i<=100: # initially i=0 exit condition of loop
    print(i)
    i=i+1 # i vlaue is incremented by 1 everytime i+=1 or i++
# line 23 to 24 (above 2 lines) called body of loop

# printing even number
# f stream function is used to combine statement with variables
# print("Even no:", var_name)
# i=1
# num=int(input("Enter your number"))
# # Program to print even and odd number
# while i<=num:
#     if i%2==0:
#         print("i as even number of num")
#     if i%2!=0:
#         print(f"{i} as odd number")
#     i=i+1

#[Note- first it will check in line no.21 1< 100 if condition is true then print 1 then line no. 23 adding 1 to i value then again to line no. 21]


# Syntax of while Loop with else statement:
# while condition:
#      # execute these statements
# else:
#      # execute these statements

# Here when while loop condition becomes false then only else block executes 

# Using else statement with while Loop
# The else clause is only executed when your while condition becomes false. 
# If you break out of the loop, or if an exception is raised, it won’t be executed.
 
count = 0
while (count < 3):
    count = count + 1 # count=0+1
    if count == 1: # 1 ==1 condition true means you can skip
        continue # skip this step u will not execute the line which are written after this and go to checking for condition again
    print("while loop body")
    print(count)
else:
    print("In Else Block")

count = 0
while (count < 3):
    count = count + 1
    if count == 2:
        break
    print("while loop body")
print("Outside loop") # this will always execute whether loop breaks or not
    
# for Loops are used for iterating over a sequence like lists, tuples, strings, and ranges.

# For loop allows you to apply the same operation to every item within loop.
# Using For Loop avoid the need of manually managing the index.
# For loop can iterate over any iterable object, such as dictionary, list or any custom iterators.

# Syntax:-
# for var in iterable:
#     # statements
#     # pass

# Using range() with For Loop
# The range() function is commonly used with for loops to generate a sequence of numbers. 
# It can take one, two, or three arguments:

# range(stop): Generates numbers from 0 to stop-1.
# range(start, stop): Generates numbers from start to stop-1.
# range(start, stop, step): Generates numbers from start to stop-1, incrementing by step.

# i=1 stop=10 printing till 10-1=9 steps- bydefault- step is 1 , step=2 (it will increment by 2)

for i in range(1, 10):
    if i==5 or i==3:
        continue
    print(i**2)
    if i%2==0:
        print(f"Even no. {i}, {i*2}")
    if i%2!=0:
        print(f"Odd number {i}, {i*3}")

for i in range(100):
    print(i) # printing value from 1 to 99
    # we have given only stop value, start value is 1 by default, step is 1 by default

    

for num in range(5):
    if num == 3:
        print("Found 3!")
        break
else:
    print("Loop completed without finding 3.")
# If 3 is found, the loop ends with break, and the else block does not execute.
# If 3 is not found, the else block executes.

#Using break to exit the loop 

for i in range(10): 
    if i == 5:
        break
    print(i) 
      
for i in range(10):
    if i % 2 == 0:
        continue 
    print(i)
