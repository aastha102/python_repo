# Inheritance (IS-A relationship)

class Engine:
    def start(self):
        print("Engine started")

class Car(Engine):   # Car IS-A Engine (not always logical)
    def drive(self):
        print("Car is driving")

c = Car()
c.start()
c.drive()
