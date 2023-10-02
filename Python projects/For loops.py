twenty = 20
fifty = 50
Odd = 0

for number in range(twenty, fifty):

    if number % 2 != 0:
        print(number)
        Odd = Odd + number

print("The Sum is", Odd)
