num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print("true all")
elif num % 3 == 0:
    print("True")
elif num % 5 == 0:
    print("true again")
else:
    print(num)
