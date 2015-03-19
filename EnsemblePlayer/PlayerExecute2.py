import sys
import youtube_dl
import os
import time
import urllib2
import urllib
import warnings
import pygame.mixer
import json

global replay
global prevStatus
global nextSong
global currentSongID
global uniqueID
global service
global status
global dataBaseID
global streampath
global oddEven
global songName
global artist
global volume
#device
PlayerID=1
nextSong=0
prevStatus=-2
currentSongID="0"
uniqueID=0
replay = False	
oddEven = False
volume = .5;						
#status 1=play 0=pause
#service 1=Gp 0=YT 2=SPOT

def main():	
	global nextSong
	global replay
	global prevStatus
	global uniqueID
	
	serverQuery(PlayerID,nextSong)
	print("cycle")
	if((nextSong == 1)and(uniqueID!=dataBaseID)):
		nextSong=0
	if(int(status)==1):
		if(replay):
			pygame.mixer.music.unpause()
			replay = False
			if(int(prevStatus)!=int(status)):
				print("Resuming play")
				prevStatus=status
		if(int(service) == 1):
			if dataBaseID == uniqueID:
				pass
			else:
				print("Type=Google")
				playGoogleSong(shouldBePlayingID,streampath,volume)
				uniqueID=dataBaseID
		elif(int(service) == 0):
			if dataBaseID == uniqueID:
				pass
			else:
				print("Type=YT")
				playYTSong(shouldBePlayingID,volume)
				uniqueID=dataBaseID
		elif(service == 2):
			print("Type=SPOT")
		elif(int(service) == -1):
			logout()
			pygame.mixer.music.unpause()
		else:
			print("server error or unrecognised")
	elif(int(status) == 0):
		p.set_pause(True)
		if(int(prevStatus)!=int(status)):
			print("Currently paused")
			prevStatus=status
		replay = True;
	else:
		pygame.mixer.music.pause()
		if(int(prevStatus)!=int(status)):
			print("Currently paused For Good")
			prevStatus=status

def serverQuery(id,nextSong):
	#{"entryId":185,"service":0,"username":null,"password":null,"apiId":0,"status":1}
	try:
		response = urllib2.urlopen('http://198.143.136.133//api/player.php?id='+str(id)+'&next='+str(nextSong))
	except:
		print("Error: Server didn't respond?")
	j_obj = json.load(response)
	global service
	global status
	global dataBaseID
	global streampath
	global songName
	global artist
	service = j_obj['service']
	status = j_obj['status']
	dataBaseID = j_obj['entryId']
	streampath = j_obj['url']
	songName = j_obj['songName']
	artist = j_obj['artist']
			
def playGoogleSong(songID,path,vol):	
	global currentSongID
	currentSongID=songID
	fileName = cleanFile()
	urllib.urlretrieve(path,fileName)
	playSong(fileName,vol)
	print ("Google: Now Playing " + songName + " by " + artist)
		
def sendNextSong():
	global nextSong
	print("Sending nextSong to DataBase")
	nextSong = 1

def cleanFile():
	global oddEven
	fileName = "even.mp3"
	if(oddEven):
		fileName = "odd.mp3"
	oddEven= not oddEven
	try:
		os.remove(fileName)
	except:
		pass
	return fileName
	
def playSong(song,vol):
	pygame.mixer.music.load(song)
	pygame.mixer.music.set_volume(vol)
	pygame.mixer.music.play()

def playYTSong(songID,vol):
	global currentSongID
	if(currentSongID!=songID):
		currentSongID=songID
		fileName = cleanFile()
		down(songID,fileName)
	playSong(fileName,vol)
	print("YT: Now Playing " + songName + " by " + artist)
	
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
				'audioformat' : "mp3",      # convert to mp3 
				'outtmpl': '%(id)s',		# name the file the ID of the video
				'noplaylist' : True,        # only download single song, not playlist
			}
		with youtube_dl.YoutubeDL(options) as ydl:
			ydl.download([b])
		os.rename(a, fileName)
	except:
		sendNextSong()

if(__name__ == "__main__"):
	warnings.filterwarnings("ignore")
	while True:
		main()