'''Remove unnecessary spaces from given string.'''

def removeSpaces(s):
	count = 0
	l = []
	for i in s:
		if i.isalpha():
			l.append(i)

	newStr = "".join(l)
	print newStr


s = "g  eeks   for ge  eks  "
removeSpaces(s)