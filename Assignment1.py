# Program Name: Assignment1.py
# Course: IT3883/Section 1
# Student Name: Aidan Oliver
# Assignment Number: Lab1
# Due Date: 09/05/ 2025
# Purpose: Program controls a data buffer stored as a string. User can add data, clear it, or display it.
# Resources: none

userOpt = ""
userString = ""
stringBuffer = ""


# Loops through the code unless user chooses to exit
while userOpt != "4":
    # Prints menu
    print("1. Append data to input buffer.")
    print("2. Clear the input buffer.")
    print("3. Display the input buffer.")
    print("4. Exit.")
    userOpt = input("Enter your choice: ")
    # Appends data to stringBuffer
    if userOpt == "1":
        userString = input("Enter your data: ")
        stringBuffer += userString
    # Clears stringBuffer
    if userOpt == "2":
        print("Clearing the input buffer...")
        stringBuffer = ""
    # Displays stringBuffer
    if userOpt == "3":
        print("Displaying the input buffer...")
        print(stringBuffer)
# Closes the program (runs outside of the while loop)
exit(0)