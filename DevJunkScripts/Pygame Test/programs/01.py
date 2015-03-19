# Pygame_notes 01.py

import pygame.cdrom
pygame.cdrom.init()

a = pygame.cdrom.CD(0)
a.init()

n = a.get_numtracks()

for c in range(n):
    a.play(c)
    while a.get_busy():
        pass              

a.quit()
a = None
pygame.cdrom.quit()

