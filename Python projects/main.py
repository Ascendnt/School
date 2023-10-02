print("Enter Marks Obtained in 5 Subjects: ")

rename = int(input("Enter Marks Obtained in 5 Subjects: "))
# math = int(input(90))
# science = int(input(91))
# english = int(input(91))
# filipino = int(input(92))

avg = rename / 4

if avg >= 99:
    print("With Highest Honors")
elif avg >= 97:
    print("With High Honors")
elif avg >= 94:
    print("With Honor")
elif avg >= 89:
    print("Passed")
elif avg <= 74:
    print("Failed")
