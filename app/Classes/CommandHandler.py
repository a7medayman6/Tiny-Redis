from app.Classes.ResponseSerializer import ResponseSerializer

# echo -en "\x2b\x50\x49\x4e\x47\x0d\x0a" | nc 127.0.0.1 6379
class CommandHandler(object):
    @staticmethod
    def handleMessage(connection, msg, storage):
        
        command = msg[0].upper()
        
        if len(msg) > 1: args = msg[1:]
        else: args = []
        
        print(f"[LOG] Command: {command}, Args(if any): {args}")
        
        if command.strip() == 'PING':
            resp = CommandHandler.handlePing(connection)
        elif command.strip() == 'ECHO':
            resp = CommandHandler.handleEcho(connection, args)
        elif command.strip() == 'SET':
            resp = CommandHandler.handleSet(connection, args, storage)
        elif command.strip() == 'GET':
            resp = CommandHandler.handleGet(connection, args, storage)
        else:
            print(f"[Error] Unhandled Command")
            return -2
        
        try:
            connection.send(ResponseSerializer.serialize_string(resp))
            print(f"[Log] Response sent successfully.")
        except:
            print(f"[Error] Failed to send response to client.")
            raise ConnectionError 
        
    def handleGet(connection, args, storage):
        if len(args) < 1:
            return ""
        
        key = args[0]
        print(f"[Log] Getting the value of the key: {key}")
        
        if key not in storage._data:
            return "nil"
        
        value = storage._data[key]
        return str(value)

    def handleSet(connection, args, storage):

        if len(args) < 2:
            return ""
        
        key, value = args[0], args[1]
        print(f"[Log] Setting the key: {key} to the value: {value} ...")
        
        storage._data[key] = value
        return "OK"
    
        

    def handleEcho(connection, args):
        print(f"[Log] Sending response to an ECHO command ...")
        
        return " ".join(args)
            
        
    def handlePing(connection):
        print(f"[Log] Sending response to a PING command ...")
    
        return "PONG"
            
    
    