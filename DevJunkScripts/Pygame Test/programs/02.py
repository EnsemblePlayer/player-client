# Pygame_notes 02.py

import os
import random
import pygame.cdrom
import pygame.mixer

songlist = []

def get_songs(p):
    a = os.listdir(p)
    for x in a:
        if x[-4:].upper() == '.WAV'\
        or x[-4:].upper() == '.MP3'\
        or x[-4:].upper() == '.OGG':
            songlist.append(os.path.join(p,x))
        elif '.' not in x:
            try:
                new_p = os.path.join(p,x)
                get_songs(new_p)
            except WindowsError:
                continue

def main():
    pygame.cdrom.init()
    a = pygame.cdrom.CD(1)
    drv_name = a.get_name()
    get_songs(drv_name)
    random.shuffle(songlist)
    pygame.mixer.init(22050,-16,2,2048)
    for song in songlist:
        try:
            pygame.mixer.music.load(song)
            print'Now playing......',song
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pass
        except RuntimeError:
            print'Could not load...',song
            continue
    pygame.mixer.quit()
    a.quit()
    a = None
    pygame.cdrom.quit()

if __name__ == '__main__': main()
