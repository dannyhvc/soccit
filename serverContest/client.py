import socket
import threading
from typing import Dict
import projcommon as common

HEADERSIZE: int = 10
# AF_INET = IPv4
# SOCK_STREAM = TCP
s: socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

# while True:
#     full_msg = ''
#     new_msg = True
#     msglen: int = 0
#     while True:
#         #packet recieving size
#         # how many bytes (chunks) to send at a time
#         msg = s.recv(16) 
#         if new_msg:
#             print("new msg len:",msg[:HEADERSIZE])
#             msglen = int(msg[:HEADERSIZE])
#             new_msg = False
#         print(f"full message length: {msglen}")
#         full_msg += msg.decode("utf-8")
#         print(len(full_msg))
#         if len(full_msg)-HEADERSIZE == msglen:
#             print("full msg recvd")
#             print(full_msg[HEADERSIZE:])
#             new_msg = True

class ClientSocket(socket.socket, threading.Thread):
    def __init__(self, func: function):
        socket.socket.__init__(self)
        self.__runMethod: function = func
        self.__dataStream: Dict = None  # filtered if no

    @property
    def runMethod(self):
        return self.__runMethod

    @property
    def dataStream(self):
        return self.__dataStream

    def run(self):
        self.runMethod() 