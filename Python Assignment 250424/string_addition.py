def string_addition(string):
	if len(string) > 3:
		return string + "ing"

	else: 
		string_addition(string)
	return string + "ly"
	
	if len(string)< 3:
		return string
	
print(string_addition("faith"))
print(string_addition("faithing"))
print(string_addition("fa"))