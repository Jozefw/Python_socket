import socket

#create socket instance for client

socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 8008

#connect to socket server

socket_client.connect((host,port))