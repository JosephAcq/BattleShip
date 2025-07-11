import socket

host = 'localhost'  # or localhost for testing
port = 5050             # ngrok-assigned port

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

print("Connected to server.")
client_socket.sendall(b"Ready to play")
response = client_socket.recv(1024)
print("Server says:", response.decode())

client_socket.close()