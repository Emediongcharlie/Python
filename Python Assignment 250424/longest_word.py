def longest_word(string):
	max = len(string[0])
	temp = string[0]
	for i in string:
		if(len(i) > max):
			max = len(i)
			temp = i
		return max, temp

print(longest_word(['emediong','bassey','charlie','come', 'deeper']))