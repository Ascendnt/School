numbers = []
num = int(input("Enter number of elements: "))
for i in range(1, num+1):
    listElements=int(input("Enter element %d: "%i))
    numbers.append(listElements)

evenList=[]
oddList=[]

for j in numbers:
    if j % 2 == 0:
        evenList.append(j)
    else:
        oddList.append(j)

print("Even number list: ", evenList)
print("Odd number list: ", oddList)
