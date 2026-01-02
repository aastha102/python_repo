class A:
    num=50

    def __init__(self):
        self.num=90

class C(A):
    def __init__(self):
        print("In C")
c=C()
print(A().num)
print(c.num) # print 90 when c constructor not there otherwise 50

# how to acccess both parent and child constructor. - using super()

class A:
    num=50

    def __init__(self):
        # protected variable- It can be modified or accessible in child class
        self._num=90
        print("In A")

class C(A):
   

    def __init__(self):
        print(super().num) # it does nothing - no use
        super().__init__()
        self.num=75 # overriding num value of parent class constructor
        self.count=89
        print("In C")
c=C()
print(c)
print(c.num)