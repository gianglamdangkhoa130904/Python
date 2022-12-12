import random

while True:
	print("[" + "Welcome to Game Keo-Bua-Bao".center(30) + "]" + "\n")
	i = "Yes"
	if(i == "Yes"):
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
		
		if ("Bua"in man):
			if (robot == "Búa"):
				Kq = "Draw"
			if (robot == "Kéo"):
				Kq = "Win"
			if (robot == "Bao"):
				Kq = "Defeat"
		if ("Keo" in man):
			if (robot == "Búa"):
				Kq = "Defeat"
			if (robot == "Kéo"):
				Kq = "Draw"
			if (robot == "Bao"):
				Kq = "Win"
		if ("Bao" in man):
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

	i = input("Continue(Yes or No): ")
	if (i == "No"):
		break;
		

