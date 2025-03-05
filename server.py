import socket
import pyodbc

server = 'localhost'
database = 'Test'
username = 'vlad'
password = 'admin'

dsn = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};Trusted_Connection=yes;'

HOST = "127.0.0.1"
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("Server is listening...")

connect, address = server.accept()
print(f"Connection from {address} has been established!")

while True:
    try:
        data = connect.recv(1024).decode()
        if not data:
            print("No data received. Closing connection...")
            break

        print(f"Data from the client: {data}")

        try:
            conn = pyodbc.connect(dsn)
            cursor = conn.cursor()

            cursor.execute("SELECT TOP 10 * FROM Calculate")
            rows = cursor.fetchall()

            print("Data from the database:")
            for row in rows:
                print(row)

            insert_query = "INSERT INTO Calculate ([Result]) VALUES (?)"
            values = (data)
            cursor.execute(insert_query, values)
            conn.commit()

            print("Data has been inserted successfully!")

            cursor.close()
            conn.close()
        except Exception as e:
            print(f"Database error: {e}")
            break
    except Exception as e:
        print(f"error: {e}")
        break

connect.close()
server.close()
print("Server has been closed.")