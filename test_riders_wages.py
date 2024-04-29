from back_to_sender import riders_wages
from minimum_number import minimum_number

def test_riders_wages_function():
	assert riders_wages(80) == 45000
	assert riders_wages(25) == 9000
	assert riders_wages(30) != 9000
	assert riders_wages(55) == 16000
	assert riders_wages(65) == 21250

def test_minimum_numbers_function():
	assert minimum_number(2,4,7) == 2
	assert minimum_number(3,7,1) != 7