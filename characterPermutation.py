#!/usr/bin/python
# Author : Grace M. Rodriguez
# CCOM5035: Dr. Yiannis Koutis
# Assigment 4
# Receive help from Jonathan Medina, 

#This was more and assigment problem, but it was interesting noverthless.
# Problem: Using your favorite language, write a program that takes as input an array of distinct characters 
#(e.g. [’a’,’c’,’d’]) and an integer k, and outputs a list of all possible strings consisting 
# of exactly k characters from the input. Each possible string should appear only once in the output.

newString = raw_input("Please write a string: ")


k = input("Please write an integer: ")

#Convert the given string into an array of characters
charList = list(newString)

listOfStrings = []
tempString = ''

#The function will receieve as parameters the list of characters and the length of k
def appendChars(charList,k):
	result = []
	#State the base case. If k = 0, then return nothing. 
	if k == 0:
		return []
	#If the length of k = 1, then just return the list of characters	
	elif k == 1:
		return charList
	#The else statement recursively matches each character with each other 
	#to make the permutations
	else:
		var = appendChars(charList,k-1)
		for i in charList:
			for j in var:
				result.append(i+j)	
		return result

stringlist = appendChars(charList,k)

for i in range(0,len(stringlist)):
	print stringlist[i]
print "Amount of permutations: ", len(stringlist)