# Define a Circle class to create a circle with radius r using the constructor. Define an Area()method for the class which calculates the area of circle. Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.

class Circle:
    def __init__(self, r):
        self.radius = r
        
    def area(self):
        return 3.14 *self.radius **2
    
    def perimeter(self):
        return 2 *3.14 *self.radius


c1 = Circle(7)
print(c1.area())
print(c1.perimeter())