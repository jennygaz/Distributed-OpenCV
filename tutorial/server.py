import socket
import time

server_socket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
host = socket.gethostname()
port = 9999
server_socket.bind( (host, port) )

