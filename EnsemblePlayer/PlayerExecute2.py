import sys
import youtube_dl
import os
import time
import urllib2
import urllib
import warnings
import pygame.mixer
import json
from subprocess import call

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
global startTime
global maxTime
#device
PlayerID=1
nextSong=0
prevStatus=-2
currentSongID="0"
uniqueID=0
replay = False	
oddEven = False
volume = .05
#status 1=play 0=pause
#service 1=Gp 0=YT 2=SPOT

def main():	
	global nextSong
	global replay
	global prevStatus
	global uniqueID
	
	serverQuery(PlayerID,nextSong)
	if((nextSong == 1)and(uniqueID!=dataBaseID)):
		nextSong=0
		print "next song reset"
	if(int(status)==1):
		if(replay):
			pygame.mixer.music.unpause()
			replay = False
			if(int(prevStatus)!=int(status)):
				print("Resuming play")
				prevStatus=status
		if(int(service) == 1):
			if dataBaseID == uniqueID:
				checkPlayerStatus()
			else:
				print("Type=Google")
				playGoogleSong(streampath,volume)
				uniqueID=dataBaseID
		elif(int(service) == 0):
			if dataBaseID == uniqueID:
				checkPlayerStatus()
			else:
				print("Type=YT")
				playYTSong(streampath,volume)
				uniqueID=dataBaseID
		elif(service == 2):
			print("Type=SPOT")
		elif(int(service) == -1):
			logout()
			pygame.mixer.music.unpause()
		else:
			print("server error or unrecognised")
	elif(int(status) == 0):
		pygame.mixer.music.pause()
		if(int(prevStatus)!=int(status)):
			print("Currently paused")
			prevStatus=status
		replay = True;
	else:
		pygame.mixer.music.pause()
		if(int(prevStatus)!=int(status)):
			print("Currently paused For Good")
			prevStatus=status

def checkPlayerStatus():
	if(int(status)==0):#paused
		return
	if(not pygame.mixer.music.get_busy()): #not busy
		if((time.time()-startTime)>=maxTime):
			print "song finished"
			sendNextSong()
			
def serverQuery(id,nextSong):
	count = 0
	while (count<5):
		try:
			response = urllib2.urlopen('http://198.143.136.133//dev/api/player.php?id='+str(id)+'&next='+str(nextSong))
			count=6
		except:
			print("Error: Server didn't respond?")
			print("Trying again")
			count+=1
	if(count==5):
		return
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
	global maxTime
	maxTime=0
	#maxTime = j_obj['length']
			
def playGoogleSong(path,vol):	
	global currentSongID
	currentSongID=path
	fileName = cleanFile()
	global startTime
	try:
		urllib.urlretrieve(path,fileName)
	except:
		print "error downloading google song"
	try:
		playSong(fileName,vol)
		startTime = time.time()
	except:
		print "error playing google song"
		sendNextSong()
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
		print "removing "+fileName+" file"
		os.remove(fileName)
	except:
		print "error cleaning "+str(fileName)+" file"
	return fileName
	
def playSong(song,vol):
	print "Playing "+str(song)
	pygame.mixer.music.load(song)
	pygame.mixer.music.set_volume(vol)
	pygame.mixer.music.play()

def playYTSong(songID,vol):
	global currentSongID
	currentSongID=songID
	fileName = cleanFile()
	down(songID,fileName)
	playSong(fileName,vol)
	global startTime
	startTime = time.time()
	print("YT: Now Playing " + songName + " by " + artist)
	
def delay(seconds):
	print "enter delay"
	thisTime = time.time()
	while((thisTime+seconds)>time.time()):
		pass
	print "exit delay"
	return

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
				'audioformat' : "aac",      # convert to aac 
				'outtmpl': '%(id)s',		# name the file the ID of the video
				'noplaylist' : True,        # only download single song, not playlist
			}
		with youtube_dl.YoutubeDL(options) as ydl:
			ydl.download([b])
		call(["ffmpeg", "-i",a,fileName])
		try:
			os.remove(a)
		except:
			pass
		return
	except:
		print "error downloading YT song"
		sendNextSong()
	return

if(__name__ == "__main__"):
	#warnings.filterwarnings("ignore")
	pygame.mixer.init(44100,-16,2,4096)
	cleanFile()
	cleanFile()
	while True:
		main()