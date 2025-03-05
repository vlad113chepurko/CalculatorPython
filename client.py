import socket
from tkinter import *
from tkinter import tkk
root = Tk()
root.title("Calculator")

PATH = "127.0.0.1"
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((PATH, PORT))


root.mainloop()