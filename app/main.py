# Uncomment this to pass the first stage
import socket

PORT = 6379

def main():
    server_socket = initServer(PORT)
    
    while True:
        conn, addr = server_socket.accept() # wait for client
        print(f"[Log] Client {addr} Connected to the server on port {PORT}.")
        handleConnection(conn, addr)

    
def handleConnection(conn, addr):
    msg = conn.recv(4096)
    decoded_msg = msg.decode('utf-8')
    extractMessage(msg)
    print(f"[Log] Client {addr} sent: {msg}")

    if 'ping' in decoded_msg:
        return handlePingCommand(conn)
    else:
        print(f"[Error]")
        return -1    


def extractMessage(msg):
    decoded_msg = msg.decode('utf-8')
    decoded_msg = decoded_msg.replace('\r', '').replace('\n', '')
    print(decoded_msg)
    
    return decoded_msg


def handlePingCommand(conn):
    try:
        print(f"[Log] Sending response to a ping command ...")
        conn.send(b"+PONG\r\n")
        print(f"[Log] Response sent successfully.")
        return 0
    except:
        print(f"[Error] Failed to send response to the client.")
        return -1




def initServer(port = 6379):
    
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    
    return server_socket

if __name__ == "__main__":
    main()
