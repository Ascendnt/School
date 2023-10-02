# Program Name:User's List
# Author: Kenneth A. Balantucas
# Program Details: A program that helps you to your listings
# Date Created: May 6, 2021

user_lists = []

print("Smartphone List")
print("\nManual: choose a number from 1-5 of your choice")
i = 'y'

while i == 'y':
    print("\nMenu")
    print("1. Add items onn your list.")
    print("2. Print items on your list.")
    print("3. Remove items on your list.")
    print("4. Modify/change your items on your list.")
    print("5. Exit")
    menu = int(input("Enter the number of your choice: "))

    if menu == 1:
        user_lists.append(input("What will you add? "))
        print(user_lists)
    elif menu == 2:
        print("The current lists are", user_lists)
    elif menu == 3:
        user_lists.pop(int(input("What are you going to remove? ")))
        print(user_lists)
    elif menu == 4:
        user_lists[int(input("Where will you place it? "))] = input("Write your new value: ")
        print(user_lists)
    elif menu == 5:
        break
    else:
        print("You have entered a wrong number.")
