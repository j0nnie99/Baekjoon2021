import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        a = math.pi * self.radius ** 2
        return round(a, 2) 

    def perimeter(self):
        p = 2 * math.pi * self.radius
        return round(p, 2)

class more_Circle(Circle):
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def radius(self):
        a = self.radius
        return a
    
    def color(self):
        b = self.color
        return b