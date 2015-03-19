from gmusicapi import Webclient
from gmusicapi import Mobileclient
import vlc
import urllib

email = 'tpgaubert@gmail.com'
password = 'pcbwoxdlptkennby'
device_id = '38a75eb25600784d'

web_client = Webclient()
mobile_client = Mobileclient()
p = vlc.MediaPlayer()

logged_in = web_client.login(email, password)
logged_in = mobile_client.login(email, password)
if logged_in == True:
    while True:
        song_name = raw_input("Song title: ")

        results = mobile_client.search_all_access(song_name, 1)
        song = results['song_hits'][0]
        song_id = song['track']['nid']
        song_name = song['track']['title']
        song_artist = song['track']['artist']
        stream_url = mobile_client.get_stream_url(song_id, device_id)
        
        urllib.urlretrieve (stream_url, "mp3.mp3")
        
	print ("Now Playing " + song_name + " by " + song_artist)
        p.set_mrl(stream_url)		
        p.play()
	p.set_time(30000)