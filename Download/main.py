
"""This part of the program will download hundreds of 
links from the site. The program will start my IDM 
download software and with the pyautogui module. 
thanks to this last one I will control my keyboard
and my mouse to automate
 what we must do manually."""



import pyautogui as py

from subprocess import call
from time import sleep


fichier = open("urls.txt")

#Retrieve all links
urls = fichier.readlines()

for url in urls:

	# Open the programm et control it with the keyboard
	call('C:\Program Files (x86)\Internet Download Manager\IDMan.exe')

	sleep(0.01)

	py.hotkey('winleft','up')  #Put in full screen our window

	py.click(x=0, y=65, clicks=1, interval=1, button='left') # x=0, y=65 localisation of our button for addind new url

	sleep(0.1)

	py.typewrite(url)

	sleep(0.5)

	py.press('enter')

	sleep(1)

	py.press('enter')

	pass









