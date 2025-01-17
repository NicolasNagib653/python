import pygame
pygame.init()
pygame.mixer.music.load('starwars.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()