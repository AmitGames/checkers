from socket import socket
import pygame

from checkers.client.screen import screen

HOST = 'localhost'
PORT = 5555
WIDTH = 1280
HEIGHT = 720
running = True

def main():
    s = screen(WIDTH, HEIGHT)

    with socket() as client:
        try:
            client.connect((HOST, PORT))
        except Exception as e:
            print(e)
        print(client.recv(1024).decode())
        choice = input("What Would you like to do")
        client.send("IDK".encode())
        while running:
            running = s.check_quit()




if __name__ == '__main__':
    main()
