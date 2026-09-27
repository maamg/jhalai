import math as m
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return m.pi * self.radius ** 2
    def perimeter(self):
        return 2 * m.pi * self.radius


radius = float(input("Enter the radius of the circle: "))
circle = Circle(radius)

area = circle.area()
perimeter = circle.perimeter()
