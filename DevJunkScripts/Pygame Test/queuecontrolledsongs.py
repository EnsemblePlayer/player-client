import os
import pygame.mixer
from gmusicapi import Webclient
from gmusicapi import Mobileclient
import urllib

# if using python2, the get_input command needs to act like raw_input:
#if sys.version_info[:2] <= (2, 7):
#    get_input = raw_input
#else:
#    get_input = input # python3

email = 'tpgaubert@gmail.com'
password = 'pcbwoxdlptkennby'
device_id = '38a75eb25600784d'
web_client = Webclient()
mobile_client = Mobileclient()
global oddEven
oddEven = False

def main():
	while True:
		song = getSong()
		playSong(song,.5)
		
def playSong(song,volume):
	pygame.mixer.music.load(song)
	pygame.mixer.music.set_volume(volume)
	pygame.mixer.music.play()

def checkCred():
	logged_in = web_client.login(email, password)
	log_in = mobile_client.login(email, password)
	return (logged_in and log_in)
	
def getSong():
	global oddEven
	
	song_name = raw_input("Song title: ")
	results = mobile_client.search_all_access(song_name, 1)
	song = results['song_hits'][0]
	song_id = song['track']['nid']
	song_name = song['track']['title']
	song_artist = song['track']['artist']
	stream_url = mobile_client.get_stream_url(song_id, device_id)
	print ("Now Playing " + song_name + " by " + song_artist)
	
	end = "even.mp3"
	if(oddEven):
		end = "odd.mp3"
	oddEven= not oddEven
	try:
		os.remove(end)
	except:
		pass
	urllib.urlretrieve(stream_url, end)
	return end
	
if(__name__ == "__main__"):
	pygame.mixer.init(22050,-16,2,2048)
	checkCred()
	main()
