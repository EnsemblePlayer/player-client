#import urllib.request
#import ssl
#https_sslv3_handler = urllib.request.HTTPSHandler(context=ssl.SSLContext(ssl.PROTOCOL_SSLv3))
#opener = urllib.request.build_opener(https_sslv3_handler)
#urllib.request.install_opener(opener)
#urllib.request.urlopen('https://fed.princeton.edu')
#https://www.youtube.com/watch?v=dQw4w9WgXcQ


import sys
import youtube_dl
import os

def down(a):
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
		
	os.rename(a, "youtube.mp3")	

if __name__ == "__main__":
	down(sys.argv[1])