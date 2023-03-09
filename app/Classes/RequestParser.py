class RequestParser:
    def __init__(self, buffer: str) -> None:
        self.handlers = {
            "": self.__parse_string,
            "-": self.__parse_error,
            ":": self.__parse_integer,
            "$": self.__parse_bulk_string,
            "*": self.__parse_array,
        }

        self.buffer = buffer

    def parse(self):
        print("[Log] Parsing the command ...")

        buffer_type = self.buffer[0]

        if buffer_type not in self.handlers.keys():
            print("[Error] Unknown Command Type.")
            return -1
        
        return self.handlers[buffer_type]()

    def __parse_integer(self):
        self.buffer = self.buffer[1:]
        
        integer, sep, self.buffer = self.buffer.partition("\r\n")
        
        return int(integer)

    def __parse_error(self):
        self.buffer = self.buffer[1:]
        
        error, sep, self.buffer = self.buffer.partition("\r\n")
        
        return error

    def __parse_bulk_string(self):
        self.buffer = self.buffer[1:]
        
        ln, sep, self.buffer = self.buffer.partition("\r\n")
        bulk, sep, self.buffer = self.buffer.partition("\r\n")
        
        return bulk

    def __parse_string(self):
        self.buffer = self.buffer[1:]
        
        string, sep, self.buffer = self.buffer.partition("\r\n")
        
        return string

    def __parse_array(self):
        self.buffer = self.buffer[1:]
        
        ln, sep, self.buffer = self.buffer.partition("\r\n")
        
        arr = []
        for _ in range(int(ln)):
            data = self.handlers[self.buffer[0]]()
            arr.append(data)
        
        return arr


