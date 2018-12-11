from tkinter import *
import mp3player_basic as mp3
import globalvars as gl

def createGui():
	gl.root.minsize(300,300)
	gl.root.geometry("600x400")
	gl.root.title(' Music Player ')
	
	#label = Label(gl.root, textvariable = gl.songname, width = 35)
	#label.pack()

	listbox = Listbox(gl.root)
	listbox.pack()
	for i in gl.realnames :
		listbox.insert(END,i)

	img1 = PhotoImage(file = r'C:\\Users\\Vatsalya Chaubey\\Documents\\Mp3\\images1.gif')
	nextbutton = Button(gl.root, image = img1, command = mp3.nextsong, height = 50, width = 50)
	nextbutton.pack()
	nextbutton.image = img1;

	img2 = PhotoImage(file = r'C:\\Users\\Vatsalya Chaubey\\Documents\\Mp3\\images2_1.gif')
	previousbutton = Button(gl.root, image = img2, command = mp3.prevsong, height = 50, width = 50)
	previousbutton.pack()
	previousbutton.image = img2;

	img3 = PhotoImage(file = r'C:\\Users\\Vatsalya Chaubey\\Documents\\Mp3\\pause.gif')
	img4 = PhotoImage(file = r'C:\\Users\\Vatsalya Chaubey\\Documents\\Mp3\\play.gif')
	pausebutton = Button(gl.root, image = img3, command = mp3.pause_play, height = 50, width = 50)
	pausebutton.pack()

	gl.root.mainloop()