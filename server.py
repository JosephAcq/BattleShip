import socket

# BOOT UP SERVER.PY THEN CLIENT.PY IN SEPERATE TERMINALS TO AFFIRM CONNECTION

print("Starting server.py")

# DO NOT REMOVE CODE UNDERNEATH-- CRUCIAL TO CONNECTION
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 5050)) 
server_socket.listen(1)
print("Waiting for connection...")
conn, addr = server_socket.accept()
# UP TO HERE

print("Connected by", addr)

# Closes the connection when done
conn.close()
