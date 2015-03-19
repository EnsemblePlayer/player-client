import urllib2
import json

def main():
	while True:
		response = "none"
		song_name = raw_input("Continue? ")
		if(song_name == "no"):
			return
		try:
			response = urllib2.urlopen('http://198.143.136.133//api/player.php?id='+str(1)+'&next='+str(0))
		except:
			print("Error: No Response?")
			continue
		print(response)
		j_obj = json.load(response)
		print(j_obj)
	
if(__name__ == "__main__"):
	main()