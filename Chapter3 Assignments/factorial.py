numbers = int(input("Enter number:"))
factorial = 1

for number in range(1, numbers+1):
	factorial = factorial * number
print (factorial)