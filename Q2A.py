print("Please select 1 to convert yards to miles and 2 to convert miles to yards.")

usr = input("Enter the conversion choice: ")

if usr == "1":
	try:
		yards = int(input("Enter distance in yards: "))
		miles = yards / 1760
		print("Equivalent distance in miles:",miles)
	except:
		print("Please restart the program and enter numbers only as input.")
	
elif usr == "2":
	try:
		miles = int(input("Enter the distance in miles: "))
		yards = miles * 1760
		print("Equivalent distance in yards:",yards)
	except:
		print("Please restart the program and enter numbers only as input.")
	
else:
	print("Invalid input")