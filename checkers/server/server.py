# Importing some stuff
import socket
import os
import threading
# consts numbers and stuff
HOST = 'localhost'
PORT = 5555
RUN = True


def on_new_client(c):
    c.send(f"Welcome to checkers".encode())
    data = c.recv(1024).decode()
    print(data)


def main():
    ThreadCount = 0
    with socket.socket() as server:
        try:
            server.bind((HOST, PORT))
        except Exception as e:
            print(e)
        print("The server has started")
        server.listen(2)
        print("Server is listening...")
        while RUN:
            client, addr = server.accept()
            print(f"Got a connection from {addr}")
            t = threading.Thread(target=on_new_client, args=(client, ))
            t.start()
            ThreadCount += 1
            print(f"Thread number currently is: {ThreadCount}")
        server.close()


if __name__ == "__main__":
    main()
