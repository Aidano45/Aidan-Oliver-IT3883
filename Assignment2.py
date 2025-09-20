# Program Name: Assignment2.py
# Course: IT3883/Section XXX
# Student Name: Aidan Oliver
# Assignment Number: Lab2
# Due Date: 9/19/ 2025
# Purpose: Reads input from the file and separates names and grades.
# It finds the average of each students grades and returns the data in descending order.

#Reads input file and creates students array
file = open("Assignment2input.txt","r")
students = []

#Separates names from grades and calaculates the average for each student
#Adds data to students[]
for line in file:
    parts = line.strip().split()

    name = parts[0]
    score = parts[1:]

    score = [int(x) for x in score]
    average = sum(score)/len(score)

    students.append((name,average))

file.close()

#Sorts the data in descending order
students.sort(key=lambda x:x[1], reverse=True)

#Prints data in specified format
for student in students:
    print(student[0], format(student[1], '.2f'))

