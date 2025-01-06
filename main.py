import socket
    #create socket instance    
socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 8008

#bind socket to host/port
socket_server.bind((host, port))

#listen for client 
socket_server.listen()

#waiting
#accept ...this is done when the client is reaching out
client, addr = socket_server.accept()

#Server sends data to client FIRST
while True:
    data = input('Lets chat: ')
    client.sendall(str.encode(data))
    msg = client.recv(1024).decode()
    if not msg:
        break
    print(msg)
client.close()
