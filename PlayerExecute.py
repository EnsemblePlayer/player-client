import sys
import youtube_dl
import os
import time
from gmusicapi import Webclient															
from gmusicapi import Mobileclient														
import vlc
import urllib
import urllib2				

global p
global username
global successLogin
global replay
global prevStatus
global nextSong
global currentSongID
global device_id
global uniqueID
#device
PlayerID=1
nextSong=0
prevStatus=-2
currentSongID="0"
uniqueID=0
replay = False
#Google
username = ""
device_id  = '38a75eb25600784d'
successLogin = False
web_client = Webclient()											
mobile_client = Mobileclient()													

#status 1=play 0=pause
#service 1=Gp 0=YT 2=SPOT

def main():
	global nextSong	
	global prevStatus
	global replay
	global uniqueID
	response = urllib2.urlopen('http://104.236.120.99//api/player.php?id='+str(PlayerID)+'&next='+str(nextSong))
	html = response.read()
	arr = html.decode("utf-8").split("~~")
	dataBaseID = arr[0]
	serviceType = arr[1]
	user = arr[2]
	password = arr[3]
	shouldBePlayingID = arr[4]
	status = arr[5]
	if((nextSong == 1)and(uniqueID!=dataBaseID)):
		nextSong=0
	if(int(status)==1):
		if(replay):
			p.set_pause(False)
			replay = False
			if(int(prevStatus)!=int(status)):
				print("Resuming play")
				prevStatus=status
		if(int(serviceType) == 1):
			if dataBaseID == uniqueID:
				pass
			else:
				print("Type=Google")
				playGoogleSong(shouldBePlayingID,user,password)
				uniqueID=dataBaseID
		elif(int(serviceType) == 0):
			if dataBaseID == uniqueID:
				pass
			else:
				print("Type=YT")
				playYTSong(shouldBePlayingID)
				uniqueID=dataBaseID
		elif(serviceType == 2):
			print("Type=SPOT")
		elif(int(serviceType) == -1):
			logout()
			p.set_pause(False)
		else:
			print("server error or unrecognised")
	elif(int(status) == 0):
		p.set_pause(True)
		if(int(prevStatus)!=int(status)):
			print("Currently paused")
			prevStatus=status
		replay = True;
	else:
		p.set_pause(True)
		if(int(prevStatus)!=int(status)):
			print("Currently paused For Good")
			prevStatus=status
		
def playGoogleSong(songID,user,password):
	global currentSongID
	global successLogin
	global username
	global device_id
	currentSongID=songID
	if((user != username)or(successLogin!=True)):
		logout()
		try:																	
			logged_in = web_client.login(user, password)
			logged_in = mobile_client.login(user, password)
			successLogin = True
			username = user
			devices = web_client.get_registered_devices()
			valid = [device['id'][2:] + " (" + device['model'] + ")" for device in devices if device['type'] == 'PHONE']
			device_id = valid[0].split(' ', 1)[0]
		except:
			logged_in = False
			successLogin = False
			print("LoginFailed")
			print("Unexpected error:", sys.exc_info()[0])
			sendNextSong()
	if((successLogin or logged_in) == True):
		p.set_pause(True)
		stream_url = mobile_client.get_stream_url(songID, device_id)
		p.set_mrl(stream_url)
		p.play()
		print("Playing a song from Google")

def logout():
	try:
		web_client.logout()
		mobile_client.logout()
		print("logged out")
	except:
		print("error logging out")
		
def sendNextSong():
	global nextSong
	print("Sending nextSong to DataBase")
	nextSong = 1
	
def SongFinished(self, data):
	print("Song Finished")
	sendNextSong()

def playYTSong(songID):
	global currentSongID
	if(currentSongID!=songID):
		currentSongID=songID
		down(songID)
	p.set_pause(True)
	p.set_mrl("youtube.mp3")
	p.play()
	print("Playing a song from YT")
	
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
		os.rename(a, "youtube.mp3")
	except:
		sendNextSong()

if(__name__ == "__main__"):
	global p
	vlc_instance = vlc.Instance()
	p = vlc_instance.media_player_new()
	vlc_events = p.event_manager()
	vlc_events.event_attach(vlc.EventType.MediaPlayerEndReached, SongFinished, 1)
	while True:
		main()