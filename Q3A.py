while True:
	usr = input("Do you really want to run this program? (y/n) ")
	
	if (usr.lower() == "y"):
		print("You decided to leave. See you again!")
		break
	elif (usr.lower() == "n"):
		continue
	else:
		print("Invalid selection is entered")
		continue