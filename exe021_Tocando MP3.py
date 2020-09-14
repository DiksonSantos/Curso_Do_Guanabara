'''import pygame
pygame.init()
pygame.mixer.music.load('jj.mp3')
pygame.mixer.music.play()
pygame.event.wait()'''

from pygame import *

mixer.init()
mixer.music.load('Action01.mp3')
mixer.music.play()

while mixer.music.get_busy():
    time.Clock().tick(10)
