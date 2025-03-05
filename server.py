import socket

PATH = "127.0.0.1"
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((PATH, PORT))

server.listen(1)
print("Server is listening...")
client, address = server.accept()
print(f"Connection from {address} has been established!")