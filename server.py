import socket

HOST = "127.0.0.1"
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("Server is listening...")

while True:
    client_socket, addr = server.accept()

    data = client_socket.recv(1024).decode()  
    if not data:
        break

    print("Received data:", data)

    client_socket.close()  

server.close()