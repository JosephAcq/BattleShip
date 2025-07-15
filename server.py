from board import Board
import socket
import threading
# BOOT UP SERVER.PY THEN CLIENT.PY IN SEPERATE TERMINALS TO AFFIRM CONNECTION

#Code to send and receive messages, end using Ctrl+C

turn = "Player 1(host)"  

def handle_receive(conn):
    global turn
    while True:
        data = conn.recv(1024)
        if not data:
            break
        msg = data.decode()
        print("\nClient guessed: ", msg)
        
        turn = "server"     # After client's move, server's turn
        conn.sendall("WAIT".encode())

def handle_send(conn):
    global turn
    while True:
        if turn == "server":
            msg = input("Enter your attack(EX: 2 4): ")
            conn.sendall(msg.encode())
            #your_turn = False
        else:
            pass
            

print("Starting server.py")

# DO NOT REMOVE CODE UNDERNEATH-- CRUCIAL TO CONNECTION
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 5050)) 
server_socket.listen(1)
print("Waiting for connection...")
conn, addr = server_socket.accept()
# UP TO HERE

print("Connected by", addr)

threading.Thread(target=handle_receive, args=(conn,), daemon=True).start()
handle_send(conn)

# Closes the connection when done
conn.close()
