

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
    if word == "penny" or word == "pennies":
        cost = 0.01
    if word == "nickel" or word == "nickels":
        cost = 0.05
    if word == "dime" or word == "dimes":
        cost = 0.1
    if word == "quarter" or word == "quarters":
        cost = 0.25
    #Adds the cost of each coin type and how many there were in the statement to amount
    amount += count*cost
    #Resets count for each full loop iteration
    count = 0
#Prints results
print(amount)

