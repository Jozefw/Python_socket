import socket

#create socket instance for client
socket_pword_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 8888

#connect to socket server
socket_pword_client.connect((host,port))

while True:
    msg = socket_pword_client.recv(1024).decode()
    if not msg:
        break
    print(msg)
    data = input('Here is my Password: ')
    socket_pword_client.sendall(str.encode(data))
    
socket_pword_client.close();
    