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

print(f"Socket open:{addr} and connection {client}")

#Server sends data to client FIRST


server_data = "Here is your server packet"
client.sendall(str.encode(server_data))
client.close()