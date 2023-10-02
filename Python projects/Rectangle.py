class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return float(2) * (self.width + self.height)


rectangle_width = int(input("Enter a number for rectangle width: "))
print("The width of the rectangle is", float(rectangle_width))
rectangle_height = int(input("Enter a number for rectangle length: "))
print("The height of the rectangle is", float(rectangle_height))
r1 = Rectangle(rectangle_width, rectangle_height)
print("The area of the rectangle is", r1.getArea())
print("The perimeter of the rectangle is", r1.getPerimeter())
Width2 = int(input("Enter a number for the other rectangle width: "))
print("The other width of the rectangle is ", float(Width2))
Height2 = int(input("Enter a number for the other rectangle length"))
print("The other height of the rectangle is", float(Height2))
R2 = Rectangle(Width2, Height2)
print("The area of the rectangle is", R2.getArea())
print("The perimeter of the rectangle is", R2.getPerimeter())
