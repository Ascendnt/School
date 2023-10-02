# This is my first class called perimeter to solve first and use it for finding the area of a polygon later
class Polygon_Perimeter:
    def __init__(self, n, s):
        self.number_of_sides = n
        self.side_length = s

    def perimeter(self):
        return self.number_of_sides * self.side_length


# This is my second class called area and I create this for hoping to achieve a high cohesion for this code
class polygon_area:
    def __init__(self, a):
        self.apothem = a

    # In this method, I call the perimeter right after it finished its solving
    def area(self):
        return 1/2 * self.apothem * solve.perimeter()


# I created an object for the 2 classes and call them all here
print("Solving the perimeter of a n-sided polygon")

# This attribute is for solving the perimeter polygon
solve = Polygon_Perimeter(float(input("Enter a number for n-sides:")), float(input("Enter a number for side length:")))
print("The perimeter of a polygon is:", solve.perimeter())
print("")
print("Solving the area of a polygon after finding the perimeter")

# This attribute is for solving the area of a polygon and use the first first class to solve for it
solve1 = polygon_area(float(input("Enter a number for apothem:")))
print("The area of a polygon is:", solve1.area())
