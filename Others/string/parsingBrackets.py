'''Instructions: You'll be receiving a string consisting of "<"and ">" and a number n 
representing the number of times you can replace a ">" with no related opening tag with "<>". 
Determine if the string is balanced or not.
Input: a string consisting of < and > and an integer n.
output: "Balanced" if balanced, "Unbalanced" if unbalanced

example 1:
input: "<>>", 1
output: "Balanced"
example 2:
input "<>>>", 1
ouput: "Unbalanced" '''


def balanced(s,n):
	stack  = []
	count = 0 
	for i in s:
		if i == "<":
			stack.append(i)
		elif i == ">" and len(stack) > 0:
			stack.pop()
		elif i == ">":
			count +=1

	if count > n or len(stack) > 0:
		print "Unbalanced"
	else:
		print "Balanced"


s = "<>>>"
n = 1
balanced(s,n)
