import random
from time import perf_counter 

start = perf_counter()  

total_question = 0
correct_questions = 0
num1_list = []
num2_list = []
status_list = []

while total_question < 10:
	num1 = random.randint(1,50)
	num2 = random.randint(1,50)

	if num1 >= num2:
		usr = int(input(f"What is {num1} - {num2} ? "))
		
		num1_list.append(num1)
		num2_list.append(num2)

		if usr == (num1 - num2):
			print("You are correct!")
			correct_questions += 1
			status_list.append("correct")
		else:
			print("Your answer is wrong")
			print(f"{num1} - {num2} should be {num1 - num2}")		
			status_list.append("wrong")

		total_question += 1
	else:
		continue


end = perf_counter() 
print("Correct count is", correct_questions)
print(f"Test time is {int(end-start)} seconds") 

for i in range(0,10,1):
	print(f"{num1_list[i]} - {num2_list[i]} = {num1_list[i] - num2_list[i]}	\t {status_list[i]}")

