class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        return f"I'm {self.name} and I'm {self.age} years old"


class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        return "Meow"


class Dog(Pet):
    def spak(self):
        return "Bark"


p = Pet("Jerry", 22)
c = Cat("Tom", 19, "Brown")
d = Dog("Tyson", 12)
print(p.show())
print(c.color)
print(d.spak())
