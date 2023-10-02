category = int(input("Enter a number "))
NASW = 25
SW = 38
Gale = 54
Whole_gale = 72
Hurricane = 73

if category <= NASW:
    print("Not a strong wind")
elif category <= SW:
    print("Strong Wind")
elif category <= Gale:
    print("Gale")
elif category <= Whole_gale:
    print("Whole gale")
elif category >= Hurricane:
    print("Hurricane")
