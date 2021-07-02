import csv
import json
import numpy
import tensorflow as tf

class Song:
	def __init__(self,number, artist,name, dance ,energy, loud, duration):
		self.number=number
		self.artist=artist
		self.name=name
		self.dance=dance
		self.energy=energy
		self.loud=loud
		self.duration=duration
		
		
def Wishman_score(song,user):
	da=song.dance/user.dance
	en=song.energy/user.energy
	lo=song.loud/user.loud
	du=song.duration/user.duration
	
	wishman=da+(en+(lo+du))
	return wishman


#gathering data and sorting it
songs=[]
with open("songs.csv","r") as f:
	data=csv.reader(f)
	header=next(data)
	size=1
	for line in data:
		artist=line[2]
		name=line[1]
		dance=float(line[3])
		energy=float(line[4])
		loud=float(line[6])
		duration=float(line[14])
		song=Song(size,artist,name,dance,energy, loud,duration)
		songs.append(song)
		size=size+1


#crete initial play list
bluff=1

#start running loop
while(bluff>0):
	i=bluff-1
	user=Song(i,songs[i].artist, songs[i].name, songs[i].dance, songs[i].energy, songs[i].loud, songs[i].duration)
	print("currently playing:   " + user.artist + " - " + user.name)
	
	#create recomendation play list
	print("recomended play list:")
	wishmans=[]
	for song in songs:
		wishmans.append(Wishman_score(song,user))
	
	#picking the songs with the best wishmans
	#ideal song has wishmn score of 5
	#recomendation should pick songs most close to 5
	
	closeness=[]
	for wishman in wishmans:
		if(wishman<4):
			closeness.append(4-wishman)
		else:
			closeness.append(wishman-4)
		
	#picking up the songs
	song_numbers=[]
	x=0
	#those greater close, 6 songs
	sub1=closeness
	while(x<7):
		j=1
		number=0
		last=100
		for n in sub1:
			if((n<last)&(n!=-1)):
				last=n
				number=j
			else:
				pass
			j=j+1
		song_numbers.append(number)
		x=x+1
		#remove the found number
		j=1
		sub2=[]
		for k in sub1:
			if(j==number):
				sub2.append(-1)
			else:
				sub2.append(k)
			j=j+1
		sub1=sub2
		
	for n in song_numbers:
		print(str(songs[n-1].number) + "  " + songs[n-1].artist + " - " + songs[n-1].name)
	
	print("Please select song number or 0 to quit")
	bluff=int(input())
				
	





















