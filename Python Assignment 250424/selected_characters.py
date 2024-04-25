def characters(string):

	if len(string) < 2:

		return " "

	return string[0:2] + string[-2:]
	

print(characters("emediong"))
print(characters("e"))
print(characters("em"))
