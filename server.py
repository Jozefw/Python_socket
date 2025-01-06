import socket

socket_password_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 8888
password = 'tropism'

socket_password_server.bind(host,port)
socket_password_server.listen()
client,addr = socket_password_server.accept()


while True:
    pword = input('Enter Password: ')
    client.sendall(str.encode(pword))
    msg = client.recv(1024).decode()
    if not msg:
        break
    if (msg != password):
        print('incorrect password, logging out')
        client.close()
    print('That is correct, Welcome')