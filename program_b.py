# Program Name: program_b.py
# Course: IT3883/Section 01
# Student Name: Aidan Oliver
# Assignment Number: Lab04
# Due Date: 10/26/ 2025
# Purpose: Recieves string from program a, converts each character to all caps, and sends it back to program a.
import socket

HOST = '127.0.0.1'
PORT = 42000

def main():
    #Create a TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()

        print(f"Program B is listening on {HOST}:{PORT}...")

        #Accept connection
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break

                #Convert to uppercase and send back
                newS = data.decode().upper()
                conn.sendall(newS.encode())

if __name__ == "__main__":
    main()