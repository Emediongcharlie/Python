def maximum_number(numbers):
	max = numbers[1]
	for i in numbers:
		if i > max:
			max = i
		return max

numbers= [8,4,9,2,5,7,3]
print(maximum_number(numbers))