def minimun_number(number):
	minimum = number[0]
	for i in range(len(number)):
		number.sort()
		if number[i] < minimum:
			minimum = number[i]
		return minimum

print(minimun_number([8,4,9,2,5,7,3]))