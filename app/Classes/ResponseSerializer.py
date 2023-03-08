class ResponseSerializer:
    @staticmethod
    def serialize_string(data: str) -> bytes:
        return f"{data}\r\n".encode()

    @staticmethod
    def serialize_error(data: str) -> bytes:
        return f"-{data}\r\n".encode()

    @staticmethod
    def serialize_integer(data: int) -> bytes:
        return f":{data}\r\n".encode()

    @staticmethod
    def serialize_bulk_string(data: str) -> bytes:
        return f"${len(data)}\r\n{data}\r\n".encode()

    @staticmethod
    def serialize_array(data: list) -> bytes:
        pass

