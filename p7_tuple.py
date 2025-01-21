# Tuple is ordered collection of heterogeneous data
# Read only version of list
# # decalaration of tuple
t=()# empty tupple decalration
t=tuple()

# converting any data to tuple using tuple function -> tuple(iteratable data type)
t=(20, 30, 40, 'True', True)
print(t, type(t))
# Tuple Supports indexing - positive and negative
# Tuple supports slicing

# Accessing elements
print(t[2])
print(-3)
print(t[-3:])

t=(20, 30, 40)
#Unpacking of tuple
x, y, z=t # LHS should be equals to RHS 
# no. of var should be equals to tuple elements
print(x, y, z)

# packing of tuple
x=20
y=30
z=40
[20, 30, 40]

# tuple is immuatable - immutable means we can not modify the data of the tuple
# tuple does not support removing data or adding data
# t.append(90) # 'tuple' object has no attribute 'append'

# tuple takes one argument means have to pass multivalue inside ()
print(tuple((x,y,z)))
t=([10, 20], (20, 30), 30)
print(len(t)) # give the number of items in tuple
print(t.count(20)) # give the occurence of that value
print(t.count(30)) # op-1

# Packing of tuple
tup=x, y, z
print(tup)

c=(10, 20, 40, 90)
print(max(c))
print(min(c))
for i in tup:
    print(i)

tup1=([10, 20, 30], [40, 50, 60], [60, 70])
print(len(tup1)) 
tup1[0].append(90) # Here u won't get any error coz we are not increasing the length instead adding into list i.e oth index
tup1.append(90) # u will get error coz we can increase the length of existing tuple
print(tup1, len(tup1))


