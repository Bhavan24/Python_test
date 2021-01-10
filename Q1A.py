num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number : "))

num_list = [num1,num2,num3]

def square(n):
	return (n * n)

def cube(n):
	return (n * n * n)

print("Number   Square    Cube")
for i in num_list:
	print(i,"\t\t",square(i),"\t\t",cube(i))