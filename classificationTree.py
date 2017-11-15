'''Code:
class TreePrinter: 
	A class that takes a stream of pairs of strings, and prints out the tree
	represented by the input considering that each pair is a parent->child
	relationship.

Example Input: (list of tuples)
	input = [('animal','mammal'),
			 ('animal','bird'),
			 ('lifeform',animal),
			 ('cat','lion'),
			 ('mammal','cat'),
			 ('animal','fish')]

	expected output:
	lifeform
		animal
			mammal
				cat
					lion
			bird
			fish  
'''

classDict = {}

input1 = [('animal','mammal'), ('animal','bird'), ('lifeform','animal'), ('cat','lion'),('mammal','cat'),
			 ('animal','fish')]

for i in input1:
	if i[0] not in classDict.keys():



