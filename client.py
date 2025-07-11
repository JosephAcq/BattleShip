import socket

# DO NOT REMOVE CODE UNDERNEATH-- CRUCIAL TO CONNECTION
host = 'localhost' 
port = 5050 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))
# UP TO HERE

print("Connected to server.")

#Closes the connection when done
client_socket.close()