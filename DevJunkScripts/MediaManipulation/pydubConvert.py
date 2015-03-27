import os
import pygame.mixer
from pydub import AudioSegment

pygame.mixer.init(22050,8,2,2048)

global songName
global artist
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
	fileName = "sameasmp3.mp3"
	fileName = convert(fileName)
	playSong(fileName,vol)
	print("YT: Now Playing " + songName + " by " + artist)
	
def convert(fileName):
	#song = AudioSegment.from_file(fileName, "mp3")
	song = AudioSegment.from_mp3(fileName)
	fileName = fileName[:-3]+".mp3"
	print("new fileName is: "+fileName)
	song.export(fileName, format="mp3")
	return fileName
if(__name__ == "__main__"):
	main()