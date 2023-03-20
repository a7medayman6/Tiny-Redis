import socket

import threading

from app.Classes.RequestParser import RequestParser

from app.Classes.CommandHandler import CommandHandler

from app.Classes.Storage import Storage

PORT = 6379
BUFFER_SIZE = 1024

def main():
    server_socket = initServer(PORT)

    storage = Storage()

    while True:    
        conn, addr = server_socket.accept() # wait for client

        print(f"[Log] Client {addr} Connected to the server on port {PORT}.")
        
        threading.Thread(target=handleClient, args=(conn, addr, storage)).start()
        
def handleClient(conn, addr, storage):
    while True: 
        print("> ", end = '')

        while True:
            try:
                msg = conn.recv(BUFFER_SIZE)

                if not msg:
                    print(f"[LOG] Client Hang Up Connection.")
                    return -2
                
                decoded_msg = RequestParser(msg.decode()).parse()

                print(f"[Log] Client {addr} sent: {msg}, decoded message: {decoded_msg}")
                
                if decoded_msg == -1:
                    raise ValueError
                
                CommandHandler.handleMessage(conn, decoded_msg, storage)

            except ConnectionError:
                print(f"[Error] Connection Error.")
                break
            except ValueError:
                print(f"[Error] The message is not formatted correctly.")
                continue


def initServer(port = 6379):
    
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    
    return server_socket

if __name__ == "__main__":
    main()
