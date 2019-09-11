# Program to convert decimal number to binary number

# Fucntion to convert decimal to binary 
def convert(num):
	
	# Creating empty list to hold binary digits of the given number
	binary = []
	
	while num // 2 != 1:
		binary.append(num % 2)
		num = num // 2    

	return binary

# Taking user input
num = int(input("Enter number to get its binay number"))


print(convert(num))
