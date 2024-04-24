counter = 0
total = 0
smallest_number = 0
largest_number = 0
for number in range(4):
	number = int(input("Enter number:"))
	total = total + number
	counter = counter + 1
	average = total / counter
	
	#min(number)
	if number < smallest_number:
		smallest_number = number
	if number > largest_number:
		largest_number = number
print("Total is ", total)
print("Average is ", average)
print("Smallest number is ", smallest_number)
print("Largest number is ", largest_number)
