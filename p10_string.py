# String- 

# Indexing from left to right-   o, 1, 2 to 10 and so on
# Indexing from right to left - -1, -2, -3, to -10 and so on

#  0    1    2   3    4   5   6   7   8   9  10  11  12 - positive indexing

# -13  -12  -11 -10  -9  -8  -7  -6  -5  -4  -3  -2  -1 
#  p    y    t   h    o   n       s   c   r   i   p   t 

s=" " # empty string
s2="P"
s='Author'
s="Python"
# String is collection of characters we can also access one character at a time. 
print(s)
print(s[4])


# Slicing in string
# s[start: stop: step] - From where iteration starts start: by default 0 if not given,  by dafult step is 1 , Stop: stop-1 by default end of length
print(s[:])
print(s[2:])
print(s[:5])
print(s[-1])
print(s[-1:-5])
print(s[-1:-5:-1])

print(s[::-1]) # Reversing a string

# String is also an iterable in python. 
for i in s:
    # print(i)
    print(i, end="")

# Strings are immutable: Can't change the value of existing string
# s[4]='P' # 'str' object does not support item assignment

s1="Hello"
s2="World"
print(id(s1))
print(id(s2))
print(s[4])
print(s[1])

# Both the objects s1 and s2 are stored in different addresses. Now, both the strings have l and o in common. 
print(id(s1[4]))
print(id(s2[1]))
# As strings are immutable, if the values are same then the address will also be same.

# Python internally maintains a dictionary, the name of this dictionary is interned dictionary.
# All the single characters are stored as keys and address of those characters are stored as values. 

# Ways to handle a string

# Anything that is after the \ is considered to be a part of string.
s='Practice makes man \'Perfect\' '
print(s)
# If the string is enclosed within " " then we can use '' inside the string and vice versa. 
s1="Practice makes man 'Perfect' "
print(s1)

# Strings Comparison
# String comparison in python can be performed in three different ways:
# 1) Comparing Values of Strings using == operator.
# 2) Comparing References of Strings using id() function or
# is operator
# 3) Comparing String values by ignoring their cases using lower() and
# upper().

s_1="Python"
s_2="Java"
s_3="Python"
s_4="python"
if s_1==s_2:
    print("Both are equal")
else:
    print("Both are unequal") # op Coz values are different

print(s_1 is s_2) # False coz memory location are different
print(s_3 == s_4) # False Coz it is case sensitive 

#[Note-Strings in python are immutable, hence two similar stringobjects are never created in the memory rather theyare shared in the memory.
# the same string object is now shared and its address is copied in s2 which now starts pointing to the same python object.]

print(s_1 is s_3) # True
print(s_1 is s_4) # False

# String Built in Methods
# join() method- Converts list to string
lst1=["Python", "Django", "Flask"]
s=","
s1=" "
print(s.join(lst1))
print(s1.join(lst1))

# upper() function on a string converts all characters to uppercase.
# lower() function on a string converts all characters to lowercase. 

print(s_1.upper()==s_4.upper()) # True coz it first converts them to uppercase then compares

# str.lower()	Converts string to lowercase
# str.upper()	Converts string to uppercase
# str.title()	Converts first letter of each word to uppercase
# str.capitalize()	Capitalizes the first character
# str.strip()	Removes leading and trailing spaces
# str.lstrip()	Removes leading spaces
# str.rstrip()	Removes trailing spaces
# str.replace(old, new)	Replaces occurrences of old with new
# str.split(sep)	Splits the string into a list
# str.join(iterable)	Joins elements of an iterable with the string as a separator
# str.find(sub)	Finds the first occurrence of sub
# str.index(sub)	Finds the index of sub, raises an error if not found
# str.count(sub)	Counts occurrences of sub in the string
# str.startswith(prefix)	Checks if the string starts with prefix
# str.endswith(suffix)	Checks if the string ends with suffix
# str.isalpha()	Checks if all characters are alphabetic
# str.isdigit()	Checks if all characters are digits
# str.isalnum()	Checks if all characters are alphanumeric
# str.isspace()	Checks if all characters are whitespace
# str.swapcase()	Swaps uppercase to lowercase and vice versa

print(dir(str))

# Get all string methods
string_methods = [method for method in dir(str) if not method.startswith("__")]
# Raw String- Use raw strings (r"") when dealing with file paths, regex, or cases where backslashes should be treated as normal characters.
print(r"\nhii") # here \n will print in terminal
print("Hii\tBye") # here \t means space, \t will not print in terminal

# Operations on String

s1="Typing"
s2="Error"
s3=50
# [Note: For concatenate: string with string, for replication: string with non string type] 
print(s1+s2)
print(s1+s3) # String can't be concatenate to int
# print(s1*s2) # string must be multiply with non str type
print(s1*3)