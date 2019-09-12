# Program to find amicable number over a range

# Function to find sum of divisors
def sum_of_divisors(num):
	temp = 0
	for i in range(1,num):
		if num % i == 0:
			temp = temp + i 
	total.append(temp)

# list containing sum of divisors 
total = []

# List containing numbers 
number = []

# User input
num = input().split()
for i in range( int(num[0]), int(num[1]) + 1 ):
	sum_of_divisors(i)
	number.append(i)

for i in range(len(total)):
	for j in range(len(number)):
		if total[i] == number[j]:
			print("The given numbers are amicable numbers:" + str(number[i]) +", "+ str(number[j]))
			break
