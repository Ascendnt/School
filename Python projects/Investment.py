class Investment:

    def __init__(self, principal, interest):
        self.p = principal
        self.i = interest

    def value_after(self):
        n = float(input("Number of Years "))
        return self.p * (1 + self.i) ** n


result = Investment(float(input("Principal: ")), float(input("Interest: ")))
print("Result", result.value_after())
