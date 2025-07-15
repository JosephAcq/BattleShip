from board import Board
import socket
import threading

your_turn = False  # Lock until server gives turn


def handle_receive(client_socket):
    global your_turn
    while True:
        data = client_socket.recv(1024)
        if not data:
            break

        message = data.decode()
        print("\nServer:", data.decode())

        if message == "Your turn":
            your_turn = True
        elif message == "WAIT":
            your_turn = False

def handle_send(conn):
    global turn
    while True:
        if turn == "server":
            msg = input("Enter your attack (ex: 2 4): ")
            conn.sendall(msg.encode())
            turn = "client"  # Pass turn to client
        else:
            continue  # Wait for your turn

            
        #msg = input("You: ")
        #client_socket.sendall(msg.encode())

# DO NOT REMOVE CODE UNDERNEATH-- CRUCIAL TO CONNECTION
host = 'localhost' 
port = 5050 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))
# UP TO HERE

print("Connected to server.")
threading.Thread(target=handle_receive, args=(client_socket,), daemon=True).start()
handle_send(client_socket)

#Closes the connection when done
client_socket.close()
