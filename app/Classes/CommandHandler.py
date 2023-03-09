from app.Classes.ResponseSerializer import ResponseSerializer

class CommandHandler(object):
    @staticmethod
    def handleMessage(connection, msg):
        
        command = msg[0].upper()
        args = msg[1:]

        if command == 'PING':
            CommandHandler.handlePing(connection)
        elif command == 'ECHO':
            CommandHandler.handleEcho(connection, args)
        else:
            print(f"[Error] Unhandled Command")
            return -2

    def handleEcho(connection, args):
        print(f"[Log] Sending response to an ECHO command ...")
        
        try:
            connection.send(ResponseSerializer.serialize_string(" ".join(args)))
            print(f"[Log] Response sent successfully.")
            return 0
        except:
            print(f"[Error] Failed to send response to client.")
            raise ConnectionError
        
    def handlePing(connection):
        print(f"[Log] Sending response to a PING command ...")
        try:
            connection.send(ResponseSerializer.serialize_string("PONG"))
            print(f"[Log] Response sent successfully.")
            return 0
        except:
            print(f"[Error] Failed to send response to client.")
            raise ConnectionError
    