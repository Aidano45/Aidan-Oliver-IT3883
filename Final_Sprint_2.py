

amount = 0
count = 0
cost = 0

#Prompt user for input statement
print("Please enter your statement: ")
user_input = input()
words = user_input.split()

#Loops through the array of words created from the input statement
for word in words:
    #Checks if the word is a digit. Sets variable count to the amount of coins
    if word.isdigit():
        count = int(word)
        continue
    #Finds the corrosponding value for the specified coin
    #Accounts for uppercase letters
    if word.lower() == "penny" or word.lower() == "pennies":
        cost = 0.01
    if word.lower() == "nickel" or word.lower() == "nickels":
        cost = 0.05
    if word.lower() == "dime" or word.lower() == "dimes":
        cost = 0.1
    if word.lower() == "quarter" or word.lower() == "quarters":
        cost = 0.25
    #Adds the cost of each coin type and how many their were in the statement to amount
    amount += count*cost
    #Resets count for each full loop iteration
    count = 0
#Prints results formatted as X.XX
print(f"{amount:.2f}")