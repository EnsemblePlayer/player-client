import youtube_dl
import os
import pygame.mixer
import audiotools

#pygame.mixer.init(44100,-16,2,4096)
pygame.mixer.init(22050,8,2,2048)

global songName
global artist
global url
global oddEven
oddEven = True
url = "wUNYDGu_fyU"
songName = "Watksy IDGAF"
artist = "Youtube"

def main():
	while True:
		response = "none"
		song_name = raw_input("Continue? ")
		if(song_name == "no"):
			return
		playYTSong(url,.3)
	#	fileName = "odd.mp3"
	#	playSong(fileName,.3)

		
def down(a,fileName):
	try:
		os.remove(a)
	except:
		pass
	try:
		os.remove(a+".part")
	except:
		pass
	try:
		b="https://www.youtube.com/watch?v="+a
		options = {
				'format': 'bestaudio', 		# choice of quality
				'extractaudio' : True,      # only keep the audio
				'audioformat' : "aac",      # convert to mp3 
				'outtmpl': '%(id)s',		# name the file the ID of the video
				'noplaylist' : True,        # only download single song, not playlist
			}
		with youtube_dl.YoutubeDL(options) as ydl:
			ydl.download([b])
		os.rename(a, fileName)
		return
	except:
		print "error downloading YT song"
	return
	
def playSong(song,vol):
	pygame.mixer.music.load(song)
	pygame.mixer.music.set_volume(vol)
	pygame.mixer.music.play()

def playYTSong(songID,vol):
	fileName = cleanFile()
	down(songID,fileName)
	playSong(fileName,vol)
	print("YT: Now Playing " + songName + " by " + artist)
	
def cleanFile():
	global oddEven
	fileName = "even.aac"
	if(oddEven):
		fileName = "odd.aac"
	oddEven= not oddEven
	try:
		os.remove(fileName)
	except:
		pass
	return fileName
	
if(__name__ == "__main__"):
	main()