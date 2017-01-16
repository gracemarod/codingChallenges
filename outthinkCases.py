#Programming Challenge 1
# This program asks for three variables, N, p and q
# Where it prints out all the numbers in from 1 to N
# However if N is divisible by p or q, it prints out "OUT"
# IF p or q are in i, it prints out "THINK"
# and if both of these conditions are met, it prints out "OUTHINK" 

# Example: 
# INPUT: 20 3 4
# OUTPUT: 1,2,OUTHINK,OUTHINK,5,OUT,OUT,10,11,OUT,THINK,
# THINK,OUT,OUT,17,OUT,19,OUT


data = raw_input("Enter N p q: ")

new_entry = data.split("")
#save the obatined data in their respective variables
N, p , q = new_entry[0:3]
N = int(N)
p = int(p)
q = int(q)

#print N, p, q
nums_list = []

#Function that recieves the integers from 1 to N
#and the list with the same number in string and
#returns isDiv and isInNum booleans
def numCond(entry):
	isDiv = False
	isInNum =  False
	#if i is divisible by p or q
	if (i % p == 0) or (i % q == 0):
		isDiv = True
	#check if p or q are in i
	if str(p) in str(entry) or str(q) in str(entry):
		isInNum =  True
	return isDiv, isInNum

#print according conditions
for i in range(1,N+1):
	isDiv, isInNum = numCond(i)
	if isDiv == True and isInNum == False:
		print "OUT",
	elif isDiv == False and isInNum == True:
		print "THINK", 
	elif isDiv and isInNum:
		print "OUTTHINK",
	else:
		print i, 


