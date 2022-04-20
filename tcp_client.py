import argparse
import socket

DATA = b"abcdefghijklmnoprstuwxyz"


class UDPClient:
    def __init__(self, host: str, port: int):
        self._host = host
        self._port = port
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __enter__(self):
        self._socket.connect((self._host, self._port))
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._socket.close()

    def send(self, stream_data: bytes):
        self._socket.sendall(stream_data)


if __name__ == '__main__':
    parser = argparse.ArgumentParser("Send UDP data to server")
    parser.add_argument("host", type=str, help="receiver's IPv4 address")
    parser.add_argument("port", type=int, help="receiver's listening port")
    args = parser.parse_args()

    with UDPClient(args.host, args.port) as client:
        if __debug__:
            print(f"Sending data to {args.host}:{args.port}")
        client.send(DATA)