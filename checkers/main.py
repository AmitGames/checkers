from socket import socket

HOST = 'localhost'
PORT = 5555


def main():
    with socket() as client:
        client.connect((HOST, PORT))
        print(client.recv(1024).decode())
        client.send("IDK".encode())

if __name__ == '__main__':
    main()
