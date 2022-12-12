import pyttsx3
import datetime
import random
import webbrowser as wb
import os
import speech_recognition as sr

def Play():
	while True:
		print("[" + "Welcome to Game Keo-Bua-Bao".center(30) + "]" + "\n")
		print("*Note: Choose Keo/Bua/Bao")
		i= "yes"
		if("yes" in i.lower()):
			x = random.randint(1,3)
			robot = ""
			man = ""
			Kq = ""

			if (x == 1):
				robot = "Búa"
			if (x == 2):
				robot = "Kéo"
			if (x == 3):
				robot = "Bao"

			man = input("Your selection: ")
			
			if ("BUA"in man.upper()):
				if (robot == "Búa"):
					Kq = "Draw"
				if (robot == "Kéo"):
					Kq = "Win"
				if (robot == "Bao"):
					Kq = "Defeat"
			if ("KEO" in man.upper()):
				if (robot == "Búa"):
					Kq = "Defeat"
				if (robot == "Kéo"):
					Kq = "Draw"
				if (robot == "Bao"):
					Kq = "Win"
			if ("BAO" in man.upper()):
				if (robot == "Búa"):
					Kq = "Win"
				if (robot == "Kéo"):
					Kq = "Defeat"
				if (robot == "Bao"):
					Kq = "Draw"

			S = "Result: " + Kq
			M = "Your selection:" + man
			R = "Robot selection: " + robot
			print("*".ljust(32,"*"))
			print("*" + M.center(30) + "*")
			print("*" + R.center(30) + "*")		
			print("*" + S.center(30) + "*")		
			print("*".ljust(32,"*"))
		i = input("Continue: ")
		if ("no" in i.lower()):
			break;

a = pyttsx3.init()
i = 1
while(i < 2):
	print("Robot: ...")
	human = input("You: ")
	if ("hello" in human.lower()):
		robot_brain = "Hello, what is your name "
		print("Robot: "+ robot_brain)
		a.say(robot_brain)
		a.runAndWait()
		human = input("You: ")
		robot_brain = "Hello " + human
	if ("today" in human.lower()):
		x = datetime.datetime.now()
		robot_brain = str(x.strftime("%d %B,%Y"))
	if("play" in human.lower()):
		Play()
		robot_brain = "Do you like it"
		print("Robot: "+ robot_brain)
		a.say(robot_brain)
		a.runAndWait()
		human = input("You: ")
		if (human.upper() == "YES"):
			robot_brain = "I'm glad to hear that:))"
		else:
			robot_brain = "I will improve on next time:(( "
	if("google" in human.lower()):
		robot_brain = "What should I search?"
		print("Robot: "+ robot_brain)
		a.say(robot_brain)
		a.runAndWait()
		human = input("You: ")
		wb.open(f'https://www.google.com/search?q={human}')
		robot_brain = "Here you are"
	if("youtube" in human.lower()):
		robot_brain = "What should I search?"
		print("Robot: "+ robot_brain)
		a.say(robot_brain)
		a.runAndWait()
		human = input("You: ")
		wb.open(f'https://www.youtube.com/search?q={human}')
		robot_brain = "Here you are"
	if("facebook" in human.lower()):
		wb.open(f'https://www.facebook.com/search?q={human}')
		robot_brain = "Please enter your account"
		print("Robot: "+ robot_brain)
		a.say(robot_brain)
		a.runAndWait()
		human = input("You: ")
		if ("done" in human.lower()):
			os.system("taskkill /im msedge.exe /f")
		robot_brain = "What should I search?"
		print("Robot: "+ robot_brain)
		a.say(robot_brain)
		a.runAndWait()
		human = input("You: ")
		wb.open(f'https://www.facebook.com/search?q={human}')
		robot_brain = "Here you are"
	if("bye" in human.lower()):
		robot_brain= "Goodbye"
		i+=1
	
	print("Robot: "+ robot_brain)
	a.say(robot_brain)
	a.runAndWait()