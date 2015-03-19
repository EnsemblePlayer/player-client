import urllib2
import json

global service
global status
global dataBaseID
#status 1=play 0=pause
#service 1=Gp 0=YT 2=SPOT

def main():
	while True:
		response = "none"
		song_name = raw_input("Continue? ")
		if(song_name == "no"):
			return
		serverQuery(1,0)
		print(service)
		
	
def serverQuery(id,nextSong):
	#{"entryId":185,"service":0,"username":null,"password":null,"apiId":0,"status":1}
	try:
		response = urllib2.urlopen('http://198.143.136.133//api/player.php?id='+str(id)+'&next='+str(nextSong))
	except:
		print("Error: Server didn't respond?")

	j_obj = json.load(response)
	
	global service
	
	
	service = j_obj['service']
	status = j_obj['status']
	dataBaseID = j_obj['entryId']
		
if(__name__ == "__main__"):
	main()