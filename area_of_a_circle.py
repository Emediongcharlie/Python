import math

PI = 3.141592653

def circle(r, PI):
	radius = r*2
	Area_of_a_circle = PI*radius
	return f" {Area_of_a_circle:.2f}"
	
#print(circle(7, PI))

def area_of_circle(radius):
	return f"{math.pi * (radius ** 2):.2f}"

print(area_of_circle(7))
