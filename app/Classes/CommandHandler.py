from app.Classes.ResponseSerializer import ResponseSerializer

class CommandHandler(object):
    @staticmethod
    def handleMessage(connection, msg):
        
        msg_array = msg.split(" ")

        command = msg_array[0].upper()
        
        if len(msg_array) > 1: args = msg_array[1:]
        else: args = ""
        
        print(command)
        
        if command.strip() == 'PING':
            # echo -en "\x2b\x50\x49\x4e\x47\x0d\x0a" | nc 127.0.0.1 6379
            CommandHandler.handlePing(connection)
        elif command.strip() == 'ECHO':
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
    