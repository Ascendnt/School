class Iteration:
    def __init__(self, minr, maxr):  # I made a constructor for minimum and maximum of the range
        self.minimum = minr
        self.maximum = maxr

    def loop(self):
        # and I put my 2 divisible here in my methods to avoid to much characters in one line
        # in attributes
        div1 = int(input("First divisible: "))
        div2 = int(input("Second divisible: "))

        while self.minimum <= self.maximum:
            if (self.minimum % div1 == 0) & (self.minimum % div2 == 0):
                print(self.minimum)
            self.minimum += 1


# and then I create an object for the class
result = Iteration(int(input("This is for minimum range: ")), int(input("This is for maximum range: ")))
result.loop()
