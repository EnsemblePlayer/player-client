import mp3play
import sys
import os

def play(a):
	c=a[8:]+".mp3"
	print(c)
	
	path = os.path.dirname(os.path.realpath(c))+'\\'+c
	print(path)
	#mp3 = mp3play(path)
	#mp3.play()
	
if __name__ == "__main__":
	play(sys.argv[1])