# pip install pygame

import pygame

# Initialize the mixer module
pygame.mixer.init()

# Load the MP3 file
pygame.mixer.music.load("pongwall.mp3")

# Play the MP3 file
pygame.mixer.music.play()


