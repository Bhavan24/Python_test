print("""
+-------------+----------+----------+	
|Room Type    | Room Code| Charge	|
+-------------+----------+----------+
|Double Room  |	  DR	 | 12000/=  |
|Twin Room	  |	  TR	 | 17000/=  |
|Master Suite |	  MS     | 24000/=  |
+-------------+----------+----------+

+--------------+---------------+-------------+----------+
|	Months	   |	< = 2 Days |  3 – 5 Days | >5Days	|
+--------------+---------------+-------------+----------+
|Jan, Feb, Mar |		5%	   |	10%		 |	 15%	|
|Apr, May, Jun |		8%	   |	13%		 |	 18%	|
|Jul, Aug, Sep |		10%	   |	15%		 |	 20%	|
|Oct, Nov, Dec |		3%	   |	8%		 |	 11%	|
+--------------+---------------+-------------+----------+
""")

room_type = ["DR", "TR", "MS"]
months = ["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]
charge_per_day = 0

while True:
	room = input("Enter the type of room(room code): ")

	if (room.upper() in room_type):
		if (room.upper() == room_type[0]):
			charge_per_day = 12000
		elif (room.upper() == room_type[1]):
			charge_per_day = 17000
		else:
			charge_per_day = 24000
		break
	else:
		print("Invalid selection for room")
		continue

while True:
	month = input("Enter the month you wish to make the reservation: ")

	if (month.lower() in months):
		break
	else:
		print("Invalid selection for month")
		continue

while True:
	try:
		days = int(input("Enter the number of days: "))
		break
	except:
		print("Please enter integer")
		continue

while True:
	try:
		no_of_rooms = int(input("Enter the number of rooms: "))

		if no_of_rooms > 5:
			print("Invalid selection for no of rooms")
			continue
		else:
			break

	except:
		print("Please enter integer")
		continue

def getDiscount(m,d):		
	if (m == "jan" or m == "feb" or m == "mar"):
		if (d <= 2):
			disc = 5/100
		elif (d <= 5):
			disc = 10/100
		else:
			disc = 15/100

	elif (m == "apr" or m == "may" or m == "jun"):
		if (d <= 2):
			disc = 5/100
		elif (d <= 5):
			disc = 10/100
		else:
			disc = 15/100

	elif (m == "jul" or m == "aug" or m == "sep"):
		if (d <= 2):
			disc = 5/100
		elif (d <= 5):
			disc = 10/100
		else:
			disc = 15/100

	else:
		if (d <= 2):
			disc = 5/100
		elif (d <= 5):
			disc = 10/100
		else:
			disc = 15/100

	return disc

total_amount = charge_per_day * days
discount = getDiscount(month,days) * total_amount
final_amount = total_amount - discount

print("Total amount:",total_amount)
print("Discount received:",discount)
print("Total Payable:",final_amount)