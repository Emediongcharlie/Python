counter = 0
total = 0
total2 = 0


gallons_used = float(input("Enter the gallons used(-1 to end)"))
miles_driven = float(input("Enter the miles driven(-1 to end)"))

while(gallons_used != -1):

	
	miles_per_gallon = miles_driven / gallons_used
	total += miles_per_gallon
	counter = counter + 1

	gallons_used = float(input("Enter the gallons used(-1 to end)"))
	miles_driven = float(input("Enter the miles driven(-1 to end)"))
	

	
	if counter != 0:
		average = total / counter		
		print("average is ", miles_per_gallon)