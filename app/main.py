import socket

from Classes.ResponseParser import ResponseParser
from Classes.ResponseSerializer import ResponseSerializer

PORT = 6379

def main():
    server_socket = initServer(PORT)

    while True:    
        conn, addr = server_socket.accept() # wait for client
        print(f"[Log] Client {addr} Connected to the server on port {PORT}.")

        while True:
            success = handleConnection(conn, addr)

            if success == -2:
                break
    
def handleConnection(conn, addr):
    msg = conn.recv(1024)
    
    if not msg:
        return -2
    
    decoded_msg = ResponseParser(msg.decode()).parse()

    print(f"[Log] Client {addr} sent: {msg}, decoded message: {decoded_msg}")
    
    for command in decoded_msg:
        handleCommand(conn, command)
    

def handleCommand(conn, command):
    if command.upper() == 'PING':
        print(f"[Log] Sending response to a ping command ...")
        try:
            conn.send(ResponseSerializer.serialize_string("PONG"))
            print(f"[Log] Response sent successfully.")
            return 0
        except:
            print(f"[Error] Failed to send response to client.")
            return -1
    else:
        print(f"[Error] Unhandled Command")
        return -2
    


def initServer(port = 6379):
    
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    
    return server_socket

if __name__ == "__main__":
    main()
