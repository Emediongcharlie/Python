amount = int(input("Enter amount:"))
rate = 7 / 100
years = int(input("Enter the number of years:"))

count = 1

analysis = 1 + rate
analysis_two = analysis ** years
new_amount = amount * analysis_two

for money in range(years):
	new_amount = amount * analysis_two
	amount = new_amount	
	print(f' {amount:.2f}')
	count += 1

