import socket
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("400x400")
root.title("Calculator")

PATH = "127.0.0.1"
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((PATH, PORT))

# main code

operations = []

def calculate():
    try:
      expr = input.get()
      result = eval(expr)
      string = f"{expr} = {result}"
      operations.append(string)
      label_exp = Label(root, text=string, background="lightgrey")
      label_exp.pack()
    except:
       print("Error")

def send():
    client.send(str(operations).encode())
    print("Data has been sent to the server!")

greeting = Label(root, text="Welcome to the calculator!")
greeting.pack()

lable_enter = Label(root, text="Enter the expression:")
lable_enter.pack()

input = Entry(root, width=50, background="lightgrey")
input.pack()

send_btn = Button(root, text="Send", background="lightblue", command=calculate)
send_btn.pack()

send_info_to_server = Button(root, text="Send info to server", background="lightgreen", command=send)
send_info_to_server.pack()

root.mainloop()