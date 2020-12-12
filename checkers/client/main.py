# imports stuff
import sys
from socket import socket
# local imports
from checkers.client.screen import screen
from checkers.client.objects.label import *

# Consts:
# Network consts
HOST = 'localhost'
PORT = 5555

# Screen Consts
WIDTH = 1280
HEIGHT = 720

# Color Consts
white = (255, 255, 255)


def main():
    # Creates the screen
    s = screen(WIDTH, HEIGHT, "main", white)
    font = pygame.font.Font(None, 64)

    # Uses With
    # also opens the socket
    with socket() as client:
        # try except to try and connect
        try:
            client.connect((HOST, PORT))
        except Exception as e:
            print(e)

        # Receives first message from the server
        data = client.recv(1024).decode()

        # Creates a bool which determines either the screen will run or not
        run = True
        while run:
            # Shows the text sample
            t = label(data, font, WIDTH // 2, 80, s.screen)
            # Updates the display using default command from pygame
            pygame.display.update()
            # changing run variable if the user wants to quit
            run = s.check_quit()
        sys.exit()


if __name__ == '__main__':
    main()
