import socket
import threading

def handle_receive(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print("\nServer:", data.decode())

def handle_send(client_socket):
    while True:
        msg = input("You: ")
        client_socket.sendall(msg.encode())

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