from app.Classes.ResponseSerializer import ResponseSerializer

class CommandHandler(object):
    @staticmethod
    def handleCommand(connection, command):
        if command.upper() == 'PING':
            CommandHandler.handlePing(connection)
        else:
            print(f"[Error] Unhandled Command")
            return -2
        
    def handlePing(connection):
        print(f"[Log] Sending response to a ping command ...")
        try:
            connection.send(ResponseSerializer.serialize_string("PONG"))
            print(f"[Log] Response sent successfully.")
            return 0
        except:
            print(f"[Error] Failed to send response to client.")
            return -1
    