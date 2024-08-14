"""Define a class named Shape and its subclass Square.
The Square class has an init function which takes length as argument.
Both classes have an area function which can print the area of the shape where
Shape’s area is 0 by default."""


# Defining the Shape class with a default area value of 0 which would be displayed in area method
class Shape:
    def __init__(self):
        self.area_val = 0

    def area(self):
        return f'The shape area is {self.area_val}'


# Defining Square subclass with a length function that would be used in the area method
class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        self.area_val = self.length * self.length
        return f'The area of the square is {self.area_val}'


shape = Shape()
square = Square(3)

print(shape.area())
print(square.area())
