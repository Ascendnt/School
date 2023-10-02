# To use the sqrt, I call the import and use the statement cmath to gain an access to it
import cmath


# this is my parameterized constructor
class quadratic:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    # I have two methods for this class because we are finding the positive and negative of the discriminant function
    # this is the first root using positive the quadratic formula
    def x1(self):
        return (-self.b) + (cmath.sqrt(self.b ** 2 - 4 * self.a * self.c)) / (2 * self.a)

    # this is the second root using the negative quadratic formula
    def x2(self):
        return (-self.b) - (cmath.sqrt(self.b ** 2 - 4 * self.a * self.c)) / (2 * self.a)


# I created an object for this class
print("Enter a number for quadratic equation.")
# I created a variable called "solve" so I can call my class quadratic and make an input with it
solve = quadratic(float(input("For a: ")), float(input("For b: ")), float(input("For c: ")))
# The last two here is I called my two methods inside my class to solve for the quadratic equation
print("The answer for the positive quadratic equation is:", solve.x1())
print("The answer for the negative quadratic equation is:", solve.x2())
