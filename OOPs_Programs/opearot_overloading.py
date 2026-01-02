# Operator overloading in Python means giving extended meaning to the standard operators (+, -, *, etc.) 
# so that they can work with user-defined objects (classes).

class Hotel:
    def __init__(self, name, fare):
        self.hotel_name=name
        self.fare=fare

    def __gt__(self, other):
        return self.fare>other.fare
        # print("Greater")
    
h1=Hotel("kite Flyer", "45000")
h2=Hotel("Lite Shineup", "60000") 
        
print(h1>h2)

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return "Substraction method"

    def __str__(self):
        return f"Vector {self.x}"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 - v2)  # Output: Vector(4, 6)
print(v1)
print(6-4)


