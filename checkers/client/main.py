# imports stuff
import sys
from socket import socket
# local imports
from checkers.client.screen import screen
from checkers.client.objects.text_box import *

# Consts:
# Network consts
HOST = 'localhost'
PORT = 5555

# Screen Consts
WIDTH = 1280
HEIGHT = 720

# Font Consts
FONT = "Ariel"

# Color Consts
white = (255, 255, 255)


def main():
    # Creates the screen
    s = screen(WIDTH, HEIGHT, "main", white)
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
            t = text_box(data, FONT, 64, WIDTH // 2, 80, s.screen)
            # Updates the display using default command from pygame
            pygame.display.update()
            # changing run variable if the user wants to quit
            run = s.check_quit()
        sys.exit()


if __name__ == '__main__':
    main()
