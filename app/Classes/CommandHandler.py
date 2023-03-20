import time

from app.Classes.ResponseSerializer import ResponseSerializer

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
        
        value, expiry = storage._data[key][0], storage._data[key][1]

        if time.time() * 1000 > expiry:
            storage._data[key] = None
            return "nil"

        return str(value)

    def handleSet(connection, args, storage):

        if len(args) < 2:
            return ""
        
        key, value = args[0], args[1]
        expiry = time.time() * 1000 + float(args[3]) if len(args) > 3 and args[2].lower() == 'px' and args[3].isnumeric() else -1
        
        print(f"[Log] Setting the key: {key} to the value: {value} ...")
        
        storage._data[key] = (value, expiry)

        return "OK"
    
        

    def handleEcho(connection, args):
        print(f"[Log] Sending response to an ECHO command ...")
        
        return " ".join(args)
            
        
    def handlePing(connection):
        print(f"[Log] Sending response to a PING command ...")
    
        return "PONG"
            
    
    