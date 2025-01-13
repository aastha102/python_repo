# String- 

# Indexing from left to right-   o, 1, 2 to 10 and so on
# Indexing from right to left - -1, -2, -3, to -10 and so on

#  0    1    2   3    4   5   6   7   8   9  10  11  12 - positive indexing

# -13  -12  -11 -10  -9  -8  -7  -6  -5  -4  -3  -2  -1 
#  p    y    t   h    o   n       s   c   r   i   p   t 

# Example integer
num = 42

# Convert integer to string
num_str = str(num)

# Check the result
print(num_str)  # Output: '42'
print(type(num_str))  # Output: <class 'str'>

p=type(num_str)
print(p)

a=10
b=20
c=a
d=10
print(a is c)
print(d is a)

num=5
ft=2.0
val=num+ft
print(val, type(val))
print(num+ft)

# x=str(val)
# print(x, type(x))

str='Hello'
del str # it will delete the memory location of str
x=str(num)
print(x)

sentence = "This is a very long sentence that we want to " \
"split over multiple lines for better readability." 
print(sentence)

x, y, z = input("Enter two values: ").split() 
print("Number of boys: ", x) 
print("Number of girls: ", y) 

str="Bottleneck"
print(str[0])
print(str[-1])

x=input("Enter your data")[0]
