"""Author: Grace M. Rodriguez - https://github.com/gracemarod

This challenge was a bit hard to understand at first. 
 A string is given with different phrases. In the sequence of passages, any passage 
 whose text (sequence of whitespace-delimited words) contained as a sub-passage
of one or more of the other passages must be filter out.

 When comparing for containment, certain rules must be followed:
 	- The case of alphabetic characters should be ignored.
 	- Leading and trailing whitespace should be ignored.
 	- Any other block of contiguous whitespace should be treated as a single 
 	space.
 	- non-alphanumeric character should be ignored, whitespace should be
 	retained

Duplicates must also be filtered -  if two passages are considered equal with respect 
to the comparision rules listed above, only the shortest should be retained. If the 
they are also the same length, the earlier one in the sequence should be kept. The 
retained passages should be output in their original form (identical to the input
passages), and in the same order.

Example: 
INPUT: "IBM cognitive computing | IBM "cognitive" computing is a \
revolution|'IBM Cognitive Computing' is a revolution?"

OUTPUT: IBM "cognitive" computing is a revolution

"""

phrase1 = "IBM cognitive computing | IBM \"cognitive\" computing is a \
revolution|\'IBM Cognitive Computing\' is a revolution?"

phrase2 = "\"Computer Science Department\"|Computer-Science-Department|\
the \"computer science department\""

phrase3 = "IBM|IBM cognitive|IBM cognitive computing|IBM \"cognitive\" computing is a \
revolution|\'IBM Cognitive Computing\' is a revolution?"

#This function simply takes the input and saves the phrases as 
#elements in a list.
def seperatePhrases(phrase):
	newPhraseList = []
	phrase_list = phrase.split("|")
	for i in phrase_list:
		tempPhrase = ""
		#Goes throught the phrases and saves them in another list with 
		#every words lower case and taking away non alpha characters.
		for j in i:
			if j.isalpha() == False and j != " ":
				next
			elif j.isupper() :
				tempPhrase += j.lower()
			else:
				tempPhrase += j


		newPhraseList.append(tempPhrase)
	#Return both the new list and the old list to access the original phrases later.
	return newPhraseList, phrase_list


onlyAlphaList, oldPhraseList = seperatePhrases(phrase2)

def comparePhrases(onlyAlphaList,oldPhraseList):

	finalphrase = {}
	newList = []
	#Double for loop to campare each element with each other
	for i in range(len(onlyAlphaList)):
		for j in range(i+1,len(onlyAlphaList)):
			#If the phrase is a subphrase of another phrase, 
			#do nothing and keep going.
			if onlyAlphaList[i] in onlyAlphaList[j]:
				next
			#Save in a dictionary as key phrases that aren't 
			#subphrases along with the index as value
			else:
				finalphrase[onlyAlphaList[i]] = i
	#If the dictionary doesn't have any elements, get the longest phrase.
	# (not sure if this logic work)
	if len(finalphrase) == 0:
		finalphrase[max(onlyAlphaList)] = onlyAlphaList.index(max(onlyAlphaList))
				
	return finalphrase

resultDict = comparePhrases(onlyAlphaList,oldPhraseList)

for d in resultDict:
	print oldPhraseList[resultDict[d]]

