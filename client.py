import socket
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("400x300")
root.title("Calculator")

# styles

style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=5)
style.configure("TLabel", font=("Arial", 12), background="#f0f0f0")
style.configure("TEntry", font=("Arial", 12), padding=5)

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
      label_exp = ttk.Label(root, text=string, font=("Arial", 16, "bold"))
      label_exp.pack()
    except Exception as e:
       print(f"Error: {e}")

def send():
    client.send(str(operations).encode())
    print("Data has been sent to the server!")

greeting = ttk.Label(root, text="Welcome to the calculator!", font=("Arial", 16, "bold"))
greeting.pack(pady=10)

label_enter = ttk.Label(root, text="Enter the expression:")
label_enter.pack(pady=5)

input = ttk.Entry(root, width=30, font=("Arial", 14))
input.pack(pady=5)

send_btn = ttk.Button(root, text="Calculate", style="TButton", command=calculate)
send_btn.pack(pady=10, ipadx=10) 

send_info_to_server = ttk.Button(root, text="Send to Server", style="TButton", command=send)
send_info_to_server.pack(pady=5, ipadx=10)

root.mainloop()