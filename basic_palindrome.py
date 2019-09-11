# Defining a function to check if reversed number is same as the original number 
# The function returns a boolean value 
def checking(number):
	left = 0
	right = len(number)-1
	count = 0 

	# traversing the loop from both the ends and checking for same elements 

	while right >= left:
	 	if number[left] != number[right]:
	 		count = 1
	 		return False
	 		break
	 	if count == 0:
	 		return True

	 	right -= 1
 		left += 1 

#  Taking number from user
number = input()

# Checking if the condition is true or not
if checking(number):
	print("The Reversed number is same as given number")
else :
	print("The given number cannot be reversed")
