import socket
import threading
# BOOT UP SERVER.PY THEN CLIENT.PY IN SEPERATE TERMINALS TO AFFIRM CONNECTION

#Code to send and receive messages, end using Ctrl+C
def handle_receive(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print("\nClient:", data.decode())

def handle_send(conn):
    while True:
        msg = input("You: ")
        conn.sendall(msg.encode())

print("Starting server.py")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 5050)) 
server_socket.listen(1)
print("Waiting for connection...")

conn, addr = server_socket.accept()
print("Connected by", addr)

threading.Thread(target=handle_receive, args=(conn,), daemon=True).start()
handle_send(conn)

conn.close()
