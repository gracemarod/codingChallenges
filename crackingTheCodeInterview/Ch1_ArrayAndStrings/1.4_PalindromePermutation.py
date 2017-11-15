''' 1.4 Palindrome Permutation Given a string, write a function to check if it is a permutation of a palindrome.

EXAMPLE:
Input: 		"Tact Coa"
Output: 	True (permutations: "Taco cat", "atco cta", etc)
'''
import string
print "Insert a string to see if it is a permutation of a palindrome: "
phrase = raw_input()

def isPermutationOfPalindrome(phrase):

	# Make dictionary of all the letters in alphabet, the keys are False
	charDict = dict.fromkeys(string.ascii_lowercase,False) 
	inputCharList = []

	for char in phrase:
		if char.isalpha():
			inputCharList.append(char.lower())

	for i in range(0, len(inputCharList)):
		if inputCharList[i] in charDict:
		   charDict[inputCharList[i]] = not charDict[inputCharList[i]]

	print "Alphabet dictionary: ", charDict
	counter = 0
	for keys in charDict:
		if charDict[keys] == True:
			counter += 1

	if counter > 1:
		return False
	else:
		return True

result = isPermutationOfPalindrome(phrase)
print result