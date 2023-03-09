import socket

import threading

from app.Classes.ResponseParser import ResponseParser

from app.Classes.CommandHandler import CommandHandler

PORT = 6379
BUFFER_SIZE = 1024

def main():
    server_socket = initServer(PORT)

    while True:    
        conn, addr = server_socket.accept() # wait for client

        print(f"[Log] Client {addr} Connected to the server on port {PORT}.")
        
        threading.Thread(target=handleClient, args=(conn, addr)).start()
        
def handleClient(conn, addr):
    while True:
        msg = conn.recv(BUFFER_SIZE)

        if not msg:
            return -2
        
        decoded_msg = ResponseParser(msg.decode()).parse()

        print(f"[Log] Client {addr} sent: {msg}, decoded message: {decoded_msg}")
        
        for command in decoded_msg:
            CommandHandler.handleCommand(conn, command)
        

def initServer(port = 6379):
    
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    
    return server_socket

if __name__ == "__main__":
    main()
