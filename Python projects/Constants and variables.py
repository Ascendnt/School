class Variables:
    def __init__(self, integer, how_many):
        self.n = integer
        self.m = how_many

    def integer(self):

        number = str(self.n)  # from here, I convert my integer to string

        sums = self.n
        sum_string = str(self.n)

        i = 1
        while i < self.m:  # then I initialize while loop
            i += 1
            sum_string = sum_string + number  # then I concatenate the string to produce n + nn + nn... etc

            sums = sums + int(sum_string)  # then before adding, I convert again to integer
        return sums


constants = Variables(int(input("Please put an integer: ")), int(input("How many: ")))
print(constants.integer())
