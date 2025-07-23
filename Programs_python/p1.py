from collections import Counter

num1=int(input("Enter your 1st num"))
num2=int(input("Enter your 2nd num"))
product=num1*num2
sum=num1+num2
if product<=100:
    print("Product of two number is", product)
else:
    print("Sum of two num is", sum)

# Write Python code to iterate through the first 10 numbers and, in each iteration, print the sum of the current and previous number.
sum=0
previous_num=0
for i in range(10):
    current_number=i
    sum=current_number+previous_num
    print(f"Current Number {current_number} Previous Number {previous_num},  Sum: {sum} ")
    previous_num=i

# Write a Python code to accept a string from the user and display characters present at an even index number.
strg=input("Enter any string")
print("Printing only even index")
for i in strg:
    if strg.index(i)%2==0:
        print(i)
 
# Write a Python code to remove characters from a string from 0 to n and return a new string.
str="Lording"
del_str=str[0:4]
print(del_str)
del del_str

# Write a code to return True if the list’s first and last numbers are the same. If the numbers are different, return False.
numberList=[10, 20, 30, 50, 90, 80, 70]
first_num = numberList[0]
last_num = numberList[-1]
if first_num == last_num:
    print("They are equal")
else:
    print("They are not equal")

# Write a Python code to display numbers from a list divisible by 5
lst=[90, 80, 65, 44, 30]
for i in lst:
    if i%5==0:
        print(f"{i} is divisible")

# Write a Python code to find how often the substring “Emma” appears in the given string.
str_x = "Emma is good developer. Emma is a writer"
print(str_x.count("Emma"))

# Write a Python code to check if the given number is a palindrome. A palindrome number reads the same forwards and backward. For example, 545 is a palindrome number.
o_num=141
num=o_num
rev_num=0
while num>=1:
    num_=num%10
    rev_num=(rev_num*10)+num_
    num=num//10

# print()  
# if o_num==rev_num:
#     print("Pallindrome")

# Get each digit from a number in the reverse order.
num=8976
while num>0:
    num_=num%10
    num=num//10
    print(num_, end=" ")

# Generate Fibonacci series up to 15 terms - 0 1 1 2 3 5 8 13 21 so on
# logic is current + previous 1 1 for the next term= 1+1=2 
num1=0
num2=1
i=15
print(num1, num2, end=" ") # 0 1
while(i>=0):
    num1,num2=num2,num1+num2
    #1st  1 0+1=1 2nd 1 2 # 3rd 2 3 # 4th 3 5 5th 5 8
    print(num1, end= " ") # 1 
    i=i-1

# # Check if a given year is a leap year
year=int(input("Please enter your year"))
if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} it is not a leap year")

# A Prime Number is a number that can only be divided by itself and 1 without remainders (e.g., 2, 3, 5, 7, 11).
num=2
while num<=20:
    for i in range(2,num):
        if num%i==0:
            break
    else:
        print(f"{num} is prime number")
    num=num+1

# Print all alternative prime numbers 2 5 11
alt_prime=True
num=2
while num<=20:
    for i in range(2,num): # num=7 goes til 2 to 6
        if num%i==0: #  7%2
            break
    else:
        if alt_prime: # for 2 it is true , for 3 it is false, for 5 it is True
            print(f"{num} is alternative prime number") # 2 5
        alt_prime=not alt_prime # False and in next iteration True
    num=num+1

# Capitalize the first letter of each word in a string
Str="python programming language"
S_word=Str.split()
s_w=[]
print(S_word)
for i in S_word:
    s_w.append(i.capitalize())
print(s_w)
str=" ".join(s_w)
print(str)

# Accept a list of 5 float numbers as an input from the user
fl_v=input("enter number").split()
float_val=[float(fv) for fv in fl_v]
print(float_val)

#  Accept any three string from one input() call
str1, str2, str3=input("Enter three words").split()
print(str1, str2, str3)

# Write a Python program to count the total number of digits in a number using a while loop.
num=12345
count=1
rem=0
if num==0:
    print("Invalid")
while num>1:

    rev=num%10
    count=count+1
    num=num//10
print(count)

# Display a message “Done” after the successful execution of the for loop
for i in range(5):
    if i==4:
        break
else:
    print("Correct")

# Find the factorial of a given number
num=1
for i in range(5,0,-1):
    num=num*i
print(num)

# Program
x=['a', 'b', 'c', 'd']
for x[-1] in x:
    print(x[-1], end=" ")

# Print the non repeating character of the string
str="aaabbccdgggtig"
counter=Counter(str)
print(counter)
list1=list(counter.keys())

for k, v in counter.items():
    if v==1:
        print(k, v)
        break

# Reverse order of tupple
tupple=(20, 50, 70, (30, 80))
l=list(tupple)
list1=l[::-1]
list2=list1[0]
print(list2[::-1])

# Remove 2 items from the list
cars_list = ['Toyota Camry', 'Honda Accord',
             'Honda Civic', 'Toyota Corolla']
del cars_list[:2]
print(cars_list)

# create a program to find largest number
lst=[10, 90, 40, 30, 60, 7, 80, 90]
max=0
for i in lst:
    if i>max: # 10>0 new max is 10 2nd  90>10 3rd 40>90 4th 30>90
        max=i # new max=90
print(max)

# create a program for 2nd largest number
# in such sceneria where 2nd largest number is present after largest number it will not work
# lst=[10, 100, 90, 40, 30, 60, 7, 80, 90, 130, 90, 120]
# max=0
# max1=0
# for i in lst: #10 100>10 110>
#     if i>max: # 120>130 condition not true will go to elif
#         max1=max # 0 10 100
#         max=i  
lst=[10, 100, 90, 40, 30, 60, 7, 80, 90, 130, 90, 120]
max=0 # largest
max1=0 # scondlargest
for i in lst: #10 100>10 110>
    if i>max: # 120>130 condition not true will go to elif
        max1=max # 0 10 100
        max=i   #10 100 130 90 120
    elif max>i and i>max1:# 130>120 120>100
        max1=i
print(max, max1)

# explaination for 2nd largest number
#1st iteration 10>0 condition true max1=0 and max=10 check for elif
# 2nd iteration 100>10 condition true max1=10 and max=100 check for elif
#3rd iteration 90>100 , 4th 40, 5th 60, 6th 7, 7th 80, 8th 90 for all these notr satistified check for elif
# next 130>100 condition true max1=100 and max=130 check for elif
# next 90 not satisfied check for elif
# next 120>130 not satisfied go to elif 130>120 and 120>100 max1=i i.e max1=120