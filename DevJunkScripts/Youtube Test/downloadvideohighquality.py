import sys
import youtube_dl
import os

def down(a):
	b="https://www.youtube.com/"+a
	print(a)
	print(b)
	options = {
			'format': 'best', 		# choice of quality
			'recodevideo' : "mp4",      # convert to mp3 
			'outtmpl': '%(id)s',		# name the file the ID of the video
		}
	with youtube_dl.YoutubeDL(options) as ydl:
		ydl.download([b])
		

if __name__ == "__main__":
	down(sys.argv[1])
