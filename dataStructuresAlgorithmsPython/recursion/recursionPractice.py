'''Recursion practice: Various problems to solve with recursion.'''

#1. Write a recursive function which takes an integer and computes the cumulative sum of 0 to that integer
# For example, if n=4 , return 4+3+2+1+0, which is 10.
def rec_sum(n):
	if n ==0:
		return 0
	else:
		return n + rec_sum(n-1)
res1 = rec_sum(4)
print "Recursion sum where n = %s the result is %s." %(4, res1)

#2. Given an integer, create a function which returns the sum of all the individual digits in that integer. 
#For example: if n = 4321, return 4+3+2+1

def sum_func(n):
	if len(str(n)) == 1:
		return n
	else:
		return n%10 + sum_func(n/10)
res2 = sum_func(4321)
print
print "Function sum where n is %s the result is %s."%(4321,res2)

#2 Create a function called word_split() which takes in a string phrase and a set list_of_words. The function will then determine if it is possible to split the string in a way in which words can be made from the list of words. 
#You can assume the phrase will only contain words found in the dictionary if it is completely splittable.
#Examples:
# word_split('themanran',['the','ran','man']) = ['the', 'man', 'ran']
# word_split('ilovedogsJohn',['i','am','a','dogs','lover','love','John']) = ['i', 'love', 'dogs', 'John']
# word_split('themanran',['clown','ran','man']) = []

def word_split(phrase,list_of_words, output = None):
    if output == None:
    	output = []

    for word in list_of_words:
    	if word in phrase:
    		print "word: ",word
    		if phrase.startswith(word):
    			output.append(word)
    			return word_split(phrase[len(word):],list_of_words,output)
    return output

prh = 'themanran'
l = ['the','ran','man']
res3 = word_split(prh,l)
print
print "For the word split function the phrase is '%s', the dictionary is %s and the output is %s" %(prh,l,res3)
