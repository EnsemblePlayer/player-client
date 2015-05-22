import pygame.mixer
file = 'even.mp3'
pygame.mixer.init(44100,-16,2,4096)
pygame.mixer.music.load(file)
pygame.mixer.music.play()
while True:
	pass