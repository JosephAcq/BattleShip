from board import Board
import socket
import threading

turn = "server"  # Server starts first

def handle_receive(conn):
    global turn
    while True:
        data = conn.recv(1024)
        if not data:
            break
        msg = data.decode()
        print("\nClient guessed:", msg)

        # After client's move, it's the server's turn
        turn = "server"
        conn.sendall("WAIT".encode())  # Lock client

def handle_send(conn):
    global turn
    while True:
        if turn == "server":
            msg = input("Enter your attack (ex: 2 4): ")
            conn.sendall(msg.encode())
            turn = "client"  # Now it's client's turn
        else:
            continue

print("Starting server.py")

# DO NOT REMOVE CODE UNDERNEATH-- CRUCIAL TO CONNECTION
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 5050)) 
server_socket.listen(1)
print("Waiting for connection...")
conn, addr = server_socket.accept()
# UP TO HERE

print("Connected by", addr)

# Start the game by telling server it's their turn
turn = "server"  # or "client" depending on who should go first

if turn == "client":
    conn.sendall("Your turn".encode())
else:
    print("Your turn to attack!")


threading.Thread(target=handle_receive, args=(conn,), daemon=True).start()
handle_send(conn)

# Closes the connection when done
conn.close()
