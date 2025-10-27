# Program Name: program_a.py
# Course: IT3883/Section 01
# Student Name: Aidan Oliver
# Assignment Number: Lab04
# Due Date: 10/26/ 2025
# Purpose: This program takes an input from the user and sends it via network communication to program b

import socket

HOST = '127.0.0.1'
PORT = 42000

def main():
    #Create a TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        #Prompt user for input
        userS = input("Enter a string to send: ")

        #Sendd the string
        s.sendall(userS.encode())

        #Waits for response
        changedS = s.recv(1024)

        #Prints string recieved from program b
        print(f"String received from Program B: {changedS.decode()}")

if __name__ == "__main__":
    main()