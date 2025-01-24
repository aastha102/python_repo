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
print(s[:])
print(s[2:])
print(s[:5])
print(s[-1])
print(s[-1:-5])
print(s[-1:-5:-1])

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

# Anything that is after the \ is considered to be a part of string.

s='Practice makes man \'Perfect\' '
print(s)
# If the string is enclosed within „ ‟ then we can use “ ” inside the string and vice versa. 
