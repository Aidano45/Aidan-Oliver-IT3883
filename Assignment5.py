# Program Name: Assignment5.py
# Course: IT3883/Section 01
# Student Name: Aidan Oliver
# Assignment Number: Lab05
# Due Date: 11/16/ 2025
# Purpose: The program creates a database using the data provided in the input file. It then computes the averages for the temperatures on Sundays and Thursdays.
# It prints the resulting averages.

import sqlite3

#Create the database and connects to it
conn = sqlite3.connect("temperatures.db")
cursor = conn.cursor()

#Create the table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS TemperatureData (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Day_Of_Week TEXT,
        Temperature_Value REAL
    );
""")

cursor.execute("DELETE FROM TemperatureData;")

#Reads input file
input_file = "Assignment5input.txt"

#Inserts rows
with open(input_file, "r") as file:
    for line in file:
        parts = line.strip().split()
        if len(parts) != 2:
            continue  # skip bad lines

        day = parts[0]
        temp = float(parts[1])

        cursor.execute("""
            INSERT INTO TemperatureData (Day_Of_Week, Temperature_Value)
            VALUES (?, ?);
        """, (day, temp))

conn.commit()

#Computes average temperature for sundays
cursor.execute("""
    SELECT AVG(Temperature_Value) FROM TemperatureData
    WHERE Day_Of_Week = 'Sunday';
""")
avg_sunday = cursor.fetchone()[0]

#Computes average temperature for thursdays
cursor.execute("""
    SELECT AVG(Temperature_Value) FROM TemperatureData
    WHERE Day_Of_Week = 'Thursday';
""")
avg_thursday = cursor.fetchone()[0]

#Prints the averages
print(f"Average Temperature for Sunday: {avg_sunday}")
print(f"Average Temperature for Thursday: {avg_thursday}")

#Closes the connection

conn.close()
