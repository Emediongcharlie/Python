max_number = 0
second_max = 0

for number in range(10):
	number = int(input("Enter number:"))

	if number > max_number:
		max_number = number
	if second_max < max_number and second_max > number:
		second_max = number
print("maximum number is ", max_number)
print("second maximum number is ", second_max)