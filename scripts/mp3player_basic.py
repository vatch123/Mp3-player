import os
from tkinter.filedialog import askdirectory
from mutagen.id3 import ID3
import pygame
from tkinter import *
import globalvars as gl

def directoryselector():
	directory = askdirectory()
	os.chdir(directory)
	for files in os.listdir(directory) :
	
		if files.endswith(".mp3"):
			path = os.path.realpath(files)
			song = ID3(path)
			gl.realnames.append(song['TIT2'].text[0])
			gl.listofsongs.append(files)
			play(gl.listofsongs[0])	



def play(song):
	#songlabel()
	gl.a = 1
	pygame.mixer.init()
	pygame.mixer.music.load(song)
	pygame.mixer.music.play()



def nextsong() :
	gl.index+=1
	if gl.index < len(gl.listofsongs):
		play(gl.listofsongs[gl.index])
	else :
		gl.index-=1



def prevsong():
	gl.index-=1;
	if gl.index >= 0:
		play(gl.listofsongs[gl.index])
	else :
		gl.index+=1

def pause_play():
	if gl.a == 1:
		pygame.mixer.music.pause()
		gl.a ^= 1
	elif gl.a == 0:
		pygame.mixer.music.unpause()
		gl.a ^= 1

#def songlabel() :
	#gl.songname.set(gl.realnames[gl.index])