# Program Name: Assignment2.py
# Course: IT3883/Section 01
# Student Name: Aidan Oliver
# Assignment Number: Lab3
# Due Date: 10/03/ 2025
# Purpose: Program converts miles per gallon to kilometers per liter. Creates a GUI for user interaction.
import tkinter as tk

conversionFactor = 0.425143707

# Converts miles per gallon to kilometers per meter
def convert(*args):
    try:
        mpg = float(inputVar.get())
        kml = mpg * conversionFactor
        resultVar.set(f"{kml:.4f}")
    except ValueError:
        # Detects if the input is invalid
        resultVar.set("Invalid input")

# Main window
root = tk.Tk()
root.title("MPG to KM/L Converter")

# Input and result variables
inputVar = tk.StringVar()
resultVar = tk.StringVar()

# Menu
tk.Label(root, text="Miles per Gallon (mpg):").grid(row=0, column=0, padx=10, pady=10, sticky="e")
mpg_entry = tk.Entry(root, textvariable=inputVar)
mpg_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Kilometers per Liter (km/L):").grid(row=0, column=2, padx=10, pady=10, sticky="e")
tk.Label(root, textvariable=resultVar, width=20, relief="sunken").grid(row=0, column=3, padx=10, pady=10)

# Conversion happens every time text changes
inputVar.trace_add("write", convert)

# Start GUI loop
root.mainloop()