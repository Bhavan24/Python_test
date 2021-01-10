import math

num_list = []
square_list = []

for i in range(1,11,1):
	usr = float(input(f"Enter number {i}: "))
	num_list.append(usr)

sum_of_num = sum(num_list)
mean = sum_of_num / 10

for j in range(0,10,1):
	squares = num_list[j] - mean
	square_list.append(math.pow(squares,2))
	
sum_of_squares = sum(square_list)
dev = math.sqrt(sum_of_squares / 9)

print("The mean is",mean)
print("The standard deviation is",dev)

