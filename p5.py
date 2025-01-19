# card_no=int(input("please enter number from 1 to 4"))
# if card_no<=0:
#     print("you are not eligible for any game")
# else:
#     match card_no:
#         case 1:
#             print("Chess")
        
#         case 2:
#             print("Carrom")

#         case 3:
#             print("Basketball")

#         case 4:
#             print("Volleyball")


# age = 20
# s = "Adult" if age >= 18 else "Minor" # First give True condition
# # if condition age>18 is true Adult is stored into s var 
# # if age>18 is false else part execute Minor is stored into s var
# print(s)
# print("Adult" if age >= 18 else "Minor" )

# if False:
#     # Here False is 0
#     print("This will never get execute coz False value is 0 means false")
# print("This is out of if block/statement") # This part always get execute coz this is not part of if block. 
# # No effect on this print statement whether if value is true or false.

# if True:
#     print("This is always True, so if block will get execute")
# print("This is out of if block/statement")


x=10
print(type(x), id(x))
x=10.4
print(type(x), id(x))
x='tree'
print(type(x), id(x))
x="tree"
print(type(x), id(x))
x='''tree'''
print(type(x), id(x))
x=20+30j
print(type(x), id(x))

x=y=z=30

print(x, y, z)
print(id(x), id(y), id(z))
x=20
print(type(x), id(x))

str="24"
print(str*2)
print(int(str)*2)
_i=24
print(_i*2)
()

str = ''' 
This is all about python. 
python var... . 
''' 
b=20 
del str
c=str(b) 
print(c) 
# TypeError: 'str' object is not callable. 
# To resolve this use del keyword before using str function. 
# del str 
# c=str(b) 
# print(c) 

str="This is bottle" \
 "this is cup"
print(str)

n = input("How many balls? ")
n=int(n) 
print(n)