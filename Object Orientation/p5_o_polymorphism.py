class Dog:
    @classmethod
    def speak(cls):
        return "Woof!"

class Cat:
    @staticmethod
    def speak():
        return "Meow!"

def make_animal_speak(animal):
    print(animal.speak())

make_animal_speak(Dog)   # Woof!
make_animal_speak(Cat)   # Meow!
