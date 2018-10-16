'''
Write a Python class named Circle constructed by a radius and four methods
which will compute the area, the perimeter of a circle and get radius and set radius.

level: 2
'''
class Circle():
    def __init__(self, radius = 0):
        self.radius = radius
        
    def set_radius(self, radius):
        self.radius = radius
        
    def get_radius(self):
        return self.radius
    
    def perimeter(self):
        return 2 * self.radius * 3.1416
    
    def area(self):
        return self.radius ** 2 * 3.1416
    
c = Circle(3)
print(c.perimeter(), c.area())
c.set_radius(5)
print(c.perimeter(), c.area())
print(c.get_radius())


    