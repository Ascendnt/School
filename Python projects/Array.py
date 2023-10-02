# Program Name:
# Author: Kenneth A. Balantucas
# Program Details:
# Date Created: May 5, 2021

class Array:
    def __init__(self, integer):
        self.int = integer

    def manipulating_arrays(self):
        sort = sorted(self.int)
        reverse = list(reversed(self.int))
        occurrence = sort.count(input("What number are you finding? "))
        print(sort)
        print(reverse)
        print(occurrence)


print("This program will sort, reverse, and show the number of occurrence of the integer.")
print("You will be asked what integer are you finding for the number of occurrence.")
result = Array(input("Please enter any number: "))
result.manipulating_arrays()
