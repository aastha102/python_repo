class Veh:
    def __init__(self, name, color, price):
        self.name=name
        self.color=color
        self.price=price

    def get_details(self):
        print(f"name is {self.name}")
        print(f"name is {self.color}")
        print(f"name is {self.price}")

    def max_speed(self):
        print("Maximum speed is 100")

    def gear(self):
        print("Gear change is 6")

class Car(Veh):
    def max_speed(self):
        print("Maximum speed is 500")

    def gear(self):
        print("Gear change is 8")

def Object(obj):
    obj.max_speed()

Object(Car("bmw", "red", "90000"))
    