import socket

print("Starting server.py")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 5050))  # bind to local port 5000 use 'ngrok http 5000'
server_socket.listen(1)
print("Waiting for connection...")

conn, addr = server_socket.accept()
print("Connected by", addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    print("Received:", data.decode())
    conn.sendall(b'ACK')

conn.close()
