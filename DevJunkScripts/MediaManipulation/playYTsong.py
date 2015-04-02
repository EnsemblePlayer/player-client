import os
import pygame.mixer

pygame.mixer.init(44100,-16,2,4096)
#pygame.mixer.init(22050,8,2,2048)

global songName
global artist
global url
global oddEven
oddEven = True
songName = "Watksy IDGAF"
artist = "Youtube"

def main():
	while True:
		response = "none"
		song_name = raw_input("Continue? ")
		if(song_name == "no"):
			return
		playYTSong("test",.3)
	
def playSong(song,vol):
	pygame.mixer.music.load(song)
	pygame.mixer.music.set_volume(vol)
	pygame.mixer.music.play()

def playYTSong(songID,vol):
	fileName = "new.mp3"
	playSong(fileName,vol)
	print("YT: Now Playing " + songName + " by " + artist)
	
if(__name__ == "__main__"):
	main()