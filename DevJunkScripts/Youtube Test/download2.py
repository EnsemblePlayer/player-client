import sys
import youtube_dl
import os

def down(a):
	try:
		os.remove("youtube.mp3")
	except:
		pass
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
				'audioformat' : "mp3",      # convert to mp3 
				'outtmpl': '%(id)s',		# name the file the ID of the video
				'noplaylist' : True,        # only download single song, not playlist
			}
		with youtube_dl.YoutubeDL(options) as ydl:
			ydl.download([b])
		#os.rename(a, "youtube.mp3")
	except:
		sendNextSong()

if __name__ == "__main__":
	down(sys.argv[1])