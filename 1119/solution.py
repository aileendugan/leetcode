def v(s):
	s = list(s)
	check= 'aeiou'
	for letter in s:
		if letter in check:
			s.remove(letter)
	return ''.join(s)

