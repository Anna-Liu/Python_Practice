print "Welcome to my game."
def startgame():
	while True:
		start = raw_input("Start game? (Quit by pressing 'q')\n>>")

		if start.lower()== "y" or start.lower() == "yes":
			print "-"
			return False
		elif start.lower() == "n" or start.lower() == "no":
			print "That's too bad. Good bye."
			change = raw_input("Do you want to change your mind?\n>>")
			
			if change.lower() == "y" or change.lower() == "yes":
				startgame()
				return False
			else:
				print "Hmph! I didn't want to play with you anyway!"
				return False
		
		elif start.lower() == "q":
			print "Thank you for playing"
			break
		else:
			print "I did not understand that."
startgame()
